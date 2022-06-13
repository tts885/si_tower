import json
import reversion
import apps.pms.forms

from django.forms.models import model_to_dict
from django.contrib import messages
from django.core import serializers
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.shortcuts import redirect

from apps.pms.models.Work import Work
from apps.pms.models.Issue import Issue
from apps.pms.forms import WorkModelFrom
from apps.pms.forms import SelectModelFrom
from apps.pms.constant.common_cons import *
from apps.pms.constant import common_messages
from apps.commons.models.Status import Status
from reversion.models import Version,Revision
from django.shortcuts import get_object_or_404


def get_verbose_names(self,json_data, models):
        meta_fields = models._meta.get_fields()
        ret = list()
        for i, meta_field in enumerate(meta_fields):
            if i > 0:
                for json_key in json_data:
                    if json_key.replace('_id','') == meta_field.name:
                        ret.append(meta_field.verbose_name)
        return ret

@method_decorator(login_required, name='dispatch')
class SearchWork(View):

    def post(self, request, *args, **kwargs):

        result_list = Work.objects.all()
        work_form = WorkModelFrom(self.request.POST)

        if Const.SESSION_MODEL_NAME and Const.SESSION_SELECT_FORM in self.request.session:
            model_name = self.request.session[Const.SESSION_MODEL_NAME]
            select_model_form = SelectModelFrom(initial={'selectForm': self.request.session[Const.SESSION_SELECT_FORM]})
        else:
            select_model_form = SelectModelFrom()

        if self.request.method == 'POST':
            # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
            work_form.is_valid()

            self.request.session[Const.SESSION_IS_UPDATE] = Const.IS_UPDATE_YES

            # Qオブジェクトを格納するリスト
            queries = []

            # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作る
            # Qオブジェクトの引数
            q_kwargs = {}

            name = work_form.cleaned_data['disp_name']
            if name:
                q_kwargs['name__icontains'] = name

            team = work_form.cleaned_data['team']
            if team:
                q_kwargs['team'] = team

            sub_team = work_form.cleaned_data['subTeam']
            if sub_team:
                q_kwargs['subTeam'] = sub_team

            status = work_form.cleaned_data['status']
            if status:
                q_kwargs['status'] = status

            owner = work_form.cleaned_data['owner']
            if owner:
                q_kwargs['owner'] = owner

            review_assign = work_form.cleaned_data['reviewAssign']
            if review_assign:
                q_kwargs['reviewAssign'] = review_assign

            # deliverables_id = work_form.cleaned_data['deliverablesId']
            # if deliverables_id:
            #     q_kwargs['deliverablesId__icontains'] = deliverables_id

            # ここは、そのフォームに入力があった場合にのみ入る。
            # フォームが空なら、q_kwargsは空のままです。
            if q_kwargs:
                q = Q(**q_kwargs)
                queries.append(q)

        if queries:
            # filter(Q(...) | Q(...) | Q(...))を動的に行っている。
            base_query = queries.pop()
            for query in queries:
                base_query |= query
            result_list = result_list.filter(base_query)

        context = {
            'model_name': model_name,
            'select_model_form': select_model_form,
            'search_form': work_form,
            'result_list': result_list,
            'const': Const
        }
        return render(self.request, 'pms/pm/dispatch_search.html', context)


@method_decorator(login_required, name='dispatch')
class CreateWork(CreateView):
    form_class = WorkModelFrom
    template_name = 'pms/pm/dispatch_create.html'
    work = Work()

    def get_success_url(self):
        # return reverse('pms:deliverables_Update', kwargs={'pk': self.object.pk})
        return reverse('pms:select_model')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # ユーザーのidを取得してモデルのuserフィールドに格納
        # postdata.system_user = self.request.user
        # データをデータベースに登録

        with reversion.create_revision():
            # Save a new model instance.

            work = postdata
            work.save()

            # Store some meta-information.
            reversion.set_user(self.request.user)
            reversion.set_comment(common_messages.NEW_RECORD_SUCCESS)

        if Const.SESSION_IS_UPDATE in self.request.session:
            del self.request.session[Const.SESSION_IS_UPDATE]
        messages.add_message(self.request, messages.SUCCESS, common_messages.NEW_RECORD_SUCCESS)

        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


class WorkDetail(DetailView):
    model = Work
    form_class = WorkModelFrom
    template_name = Const.PM_UPDATE_URL

    def get_success_url(self):
        return reverse('pms:work_Update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        ctx = super(DetailView, self).get_context_data(**kwargs)
        ctx.update(dict(const=Const))
        return ctx


@method_decorator(login_required, name='dispatch')
class UpdateWork(UpdateView):
    model = Work
    form_class = WorkModelFrom
    template_name = 'pms/pm/dispatch_update.html'
    # work = Work()
    # 1ページに表示するレコードの件数
    # paginate_by = 1


    def get_success_url(self):
        return reverse('pms:work_Update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        result = Work.objects.get(pk=self.object.pk)
        issue_list = result.issue.all()

        instance = get_object_or_404(Work, id= self.object.pk)
        versions = Version.objects.get_for_object(instance)
   
        new_versions = list(versions)

        # ctx = super(UpdateView, self).get_context_data(**kwargs)
        ctx = super().get_context_data(**kwargs)
        ctx.update(dict(const=Const))
        ctx.update({'const': Const, 'model_name': Const.MODEL_WORK, 'result_list': issue_list,'versions':versions})

        return ctx

    def form_valid(self, form):
        work = Work.objects.get(pk=self.object.pk)
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # ユーザーのidを取得してモデルのuserフィールドに格納
        # postdata.system_user = self.request.user
        work = postdata
        work_change = work.tracker.changed()
        # データをデータベースに登録
        postdata.save()

        changed_verbose_names =get_verbose_names(self,work_change,Work)

        with reversion.create_revision():
            # Save a new model instance.
            formdata = postdata
            formdata.save()
            # Store some meta-information.
            reversion.set_user(self.request.user)
            reversion.set_comment('[' +  ']、['.join(changed_verbose_names) + ']を変更されている')

        # if SESSION_IS_UPDATE in self.request.session:
        #     del self.request.session[SESSION_IS_UPDATE]

        messages.add_message(self.request, messages.SUCCESS, common_messages.UPDATE_RECORD_SUCCESS)
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


def issue_to_dictionary(issue):
    if issue is None:
        return None

    dictionary = {"search_id": issue.id, "name": '[課題]_' + issue.name}

    return dictionary


@method_decorator(login_required, name='dispatch')
class Work_GetIssue(View):

    @staticmethod
    def post(request):

        try:
            if request.POST["search_id"] != "" and request.POST["search_id"].isdecimal() is True:
                issue = Issue.objects.get(pk=request.POST["search_id"])
            else:
                issue = None
        except Issue.DoesNotExist:
            issue = None

        issue_dictionary = issue_to_dictionary(issue)

        return JsonResponse(issue_dictionary, safe=False)


@method_decorator(login_required, name='dispatch')
class AddRelation_toWork(View):

    @staticmethod
    def post(request):
        work = Work.objects.get(pk=request.POST["index"])
        try:
            if request.POST["search_id"] != "" and request.POST["search_id"].isdecimal() is True:

                issue = Issue.objects.get(pk=request.POST["search_id"])
                work.issue.add(issue)

                with reversion.create_revision():
                    # Save a new model instance.
                    formdata = work
                    formdata.save()
                    # Store some meta-information.
                    reversion.set_user(request.user)
                    reversion.set_comment('課題(' + request.POST["search_id"] + ')の関連付けを追加しました。')

            else:
                issue = None
        except Issue.DoesNotExist:
            issue = None

        issue_dictionary = issue_to_dictionary(issue)

        return JsonResponse(issue_dictionary, safe=False)


@method_decorator(login_required, name='dispatch')
class RemoveRelation_fromWork(View):

    @staticmethod
    def get(request, object_pk, record_pk):
        work = Work.objects.get(pk=object_pk)
        try:

            issue = Issue.objects.get(pk=record_pk)
            work.issue.remove(issue)

        except Issue.DoesNotExist:
            issue = None

        return redirect('pms:work_Update', pk=object_pk)