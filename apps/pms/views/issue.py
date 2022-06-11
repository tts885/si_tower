
from tarfile import RECORDSIZE
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View,ListView, CreateView, DetailView, UpdateView
from django.db.models import Q
from django.shortcuts import redirect,render
from requests import request

from apps.pms.models.Work import Work
from apps.pms.models.Issue import Issue
from apps.pms.forms import WorkModelFrom, IssueModelFrom
from apps.pms.forms import SelectModelFrom
from apps.pms.constant.common_cons import *
from apps.pms.constant import common_messages

import reversion
import apps.pms.forms


@method_decorator(login_required, name='dispatch')
class SearchIssue(View):

    def post(self, request, *args, **kwargs):

        result_list = Issue.objects.all()
        issue_form = IssueModelFrom(self.request.POST)

        if Const.SESSION_MODEL_NAME and Const.SESSION_SELECT_FORM in self.request.session:
            model_name = self.request.session[Const.SESSION_MODEL_NAME]
            select_model_form = SelectModelFrom(initial={'selectForm': self.request.session[Const.SESSION_SELECT_FORM]})
        else:
            select_model_form = SelectModelFrom()

        if self.request.method == 'POST':
            # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
            issue_form.is_valid()

            self.request.session[Const.SESSION_IS_UPDATE] = Const.IS_UPDATE_YES

            # Qオブジェクトを格納するリスト
            queries = []

            # 各フォームの入力をもとに、Qオブジェクトとして検索条件を作る
            # Qオブジェクトの引数
            q_kwargs = {}

            name = issue_form.cleaned_data['disp_name']
            if name:
                q_kwargs['name__icontains'] = name

            team = issue_form.cleaned_data['team']
            if team:
                q_kwargs['team'] = team

            sub_team = issue_form.cleaned_data['subTeam']
            if sub_team:
                q_kwargs['subTeam'] = sub_team

            status = issue_form.cleaned_data['status']
            if status:
                q_kwargs['status'] = status

            owner = issue_form.cleaned_data['owner']
            if owner:
                q_kwargs['owner'] = owner

            # review_assign = issue_form.cleaned_data['reviewAssign']
            # if review_assign:
            #     q_kwargs['reviewAssign'] = review_assign

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
            'search_form': issue_form,
            'result_list': result_list,
            'const': Const
        }
        return render(self.request, 'pms/pm/dispatch_search.html', context)


@method_decorator(login_required, name='dispatch')
class CreateIssue(CreateView):
    form_class = IssueModelFrom
    template_name = 'pms/pm/dispatch_create.html'
    issue= Issue()

    def get_success_url(self):
        return reverse('pms:issue_Update', kwargs={'pk': self.object.pk})
        # return reverse('pms:select_model')

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # ユーザーのidを取得してモデルのuserフィールドに格納
        # postdata.system_user = self.request.user
        # データをデータベースに登録
        postdata.save()

        with reversion.create_revision():
            # Save a new model instance.

            issue = postdata
            issue.save()

            # Store some meta-information.
            reversion.set_user(self.request.user)
            reversion.set_comment(common_messages.NEW_RECORD_SUCCESS)

        if Const.SESSION_IS_UPDATE in self.request.session:
            del self.request.session[Const.SESSION_IS_UPDATE]
        messages.add_message(self.request, messages.SUCCESS, common_messages.NEW_RECORD_SUCCESS)

        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


# class WorkDetail(DetailView):
#     model = Work
#     form_class = WorkModelFrom
#     template_name = Const.PM_UPDATE_URL
#
#     def get_success_url(self):
#         return reverse('pms:work_Update', kwargs={'pk': self.object.pk})
#
#     def get_context_data(self, **kwargs):
#         ctx = super(DetailView, self).get_context_data(**kwargs)
#         ctx.update(dict(const=Const))
#         return ctx


@method_decorator(login_required, name='dispatch')
class UpdateIssue(UpdateView):
    model = Issue
    form_class = IssueModelFrom
    template_name = 'pms/pm/dispatch_update.html'

    # template_name = 'pms/pm/create/issue.html'
    # issue = Issue()
    # 1ページに表示するレコードの件数
    # paginate_by = 1

    def get_success_url(self):
        return reverse('pms:issue_Update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        result = Issue.objects.get(pk=self.object.pk)
        work_list = result.work_set.all()

        # ctx = super(UpdateView, self).get_context_data(**kwargs)
        ctx = super().get_context_data(**kwargs)
        # ctx.update(dict(const=Const))
        ctx.update({'const': Const, 'model_name': Const.MODEL_ISSUE, 'result_list': work_list})

        return ctx

    def form_valid(self, form):
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # ユーザーのidを取得してモデルのuserフィールドに格納
        # postdata.system_user = self.request.user

        # データをデータベースに登録
        postdata.save()

        with reversion.create_revision():
            # Save a new model instance.

            issue = postdata
            issue.save()
            # Store some meta-information.
            reversion.set_user(self.request.user)
            reversion.set_comment("Update revision 1")

        # if SESSION_IS_UPDATE in self.request.session:
        #     del self.request.session[SESSION_IS_UPDATE]

        messages.add_message(self.request, messages.SUCCESS, common_messages.UPDATE_RECORD_SUCCESS)
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


def work_to_dictionary(work):
    if work is None:
        return None

    dictionary = {"search_id": work.id, "name": work.name}

    return dictionary


@method_decorator(login_required, name='dispatch')
class Issue_GetWork(View):

    @staticmethod
    def post(request):
        try:
            if request.POST["search_id"] != "" and request.POST["search_id"].isdecimal() == True:
                work = Work.objects.get(pk=request.POST["search_id"])
            else:
                work = None
        except Work.DoesNotExist:
            work = None
        work_dictionary = work_to_dictionary(work)
        return JsonResponse(work_dictionary, safe=False)


class AddRelation_toIssue(View):
    @staticmethod
    def post(request):
        try:
            if request.POST["search_id"] != "" and request.POST["search_id"].isdecimal() == True:
                work = Work.objects.get(pk=request.POST["search_id"])
                issue = Issue.objects.get(pk=request.POST["index"])
                work.issue.add(issue)

            else:
                issue = None
        except Issue.DoesNotExist:
            issue = None
        work_dictionary = work_to_dictionary(issue)
        return JsonResponse(work_dictionary, safe=False)


@method_decorator(login_required, name='dispatch')
class RemoveRelation_fromIssue(View):

    @staticmethod
    def get(request, object_pk, record_pk):
        work = Work.objects.get(pk=record_pk)
        try:

            issue = Issue.objects.get(pk=object_pk)
            work.issue.remove(issue)

        except Issue.DoesNotExist:
            issue = None

        return redirect('pms:issue_Update', pk=object_pk)
