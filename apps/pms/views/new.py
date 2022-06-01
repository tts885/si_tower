import os
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

from apps.pms.forms import SelectModelFromSet
from apps.pms.forms import WorkModelFrom
from apps.pms.forms import DeliverablesModelFrom
from apps.pms.forms import IssueModelFrom
from apps.pms.forms import ScenarioModelFrom
from apps.pms.forms import BacModelFrom
from apps.pms.forms import RiskModelFrom
from apps.pms.constant.common_cons import Const
from apps.pms.models.Deliverables import Deliverables


class SelectForm:

    def getformclass(modelName):
        if modelName == Const.MODEL_PROJECT:
            form_class = WorkModelFrom

        elif modelName == Const.MODEL_TRACKER:
            form_class = WorkModelFrom

        elif modelName == Const.MODEL_DELIVERABLES:
            form_class = DeliverablesModelFrom

        elif modelName == Const.MODEL_WORK:
            form_class = WorkModelFrom

        elif modelName == Const.MODEL_SCENARIO:
            form_class = ScenarioModelFrom

        elif modelName == Const.MODEL_BAC:
            form_class = BacModelFrom

        elif modelName == Const.MODEL_ISSUE:
            form_class = IssueModelFrom

        elif modelName == Const.MODEL_RISK:
            form_class = RiskModelFrom

        elif modelName == Const.MODEL_PARENT:
            form_class = ParentModelFrom

        return form_class

    def getmodelclass(modelName):

        if modelName == Const.MODEL_PROJECT:
            s_mode = Deliverables()

        elif modelName == Const.MODEL_TRACKER:
            s_mode = Deliverables()

        elif modelName == Const.MODEL_DELIVERABLES:
            s_mode = Deliverables()

        elif modelName == Const.MODEL_WORK:
            s_mode = WorkModelFrom

        elif modelName == Const.MODEL_SCENARIO:
            s_mode = ScenarioModelFrom

        elif modelName == Const.MODEL_BAC:
            s_mode = BacModelFrom

        elif modelName == Const.MODEL_ISSUE:
            s_mode = IssueModelFrom

        elif modelName == Const.MODEL_RISK:
            s_mode = RiskModelFrom

        elif modelName == Const.MODEL_PARENT:
            s_mode = ParentModelFrom

        return s_mode


@login_required()
def select_model(request):
    # profile_list = StatusManagement.objects.all()
    formset = SelectModelFromSet(request.POST or None)
    if request.method == 'POST':
        # 全ての入力欄はrequired=Falseなので、必ずTrueになる。
        formset.is_valid()
        request.session[Const.SESSION_IS_UPDATE] = Const.IS_UPDATE_NO

        for form in formset:

            selectForm = form.cleaned_data.get(Const.SESSION_SELECT_FORM)
            model_name = form.modelNames[int(selectForm)][1]

            form_class = SelectForm.getformclass(model_name)

            #
            # if modelName == MODEL_PROJECT:
            #     form_class = WorkModelFrom
            #
            # elif modelName == MODEL_TRACKER:
            #     form_class = WorkModelFrom
            #
            # elif modelName == MODEL_DELIVERABLES:
            #     form_class = DeliverablesModelFrom
            #
            # elif modelName == MODEL_WORK:
            #     form_class = WorkModelFrom
            #
            # elif modelName == MODEL_SCENARIO:
            #     form_class = ScenarioModelFrom
            #
            # elif modelName == MODEL_BAC:
            #     form_class = BacModelFrom
            #
            # elif modelName == MODEL_ISSUE:
            #     form_class = IssueModelFrom
            #
            # elif modelName == MODEL_RISK:
            #     form_class = RiskModelFrom
            #
            # elif modelName == MODEL_PARENT:
            #     form_class = ParentModelFrom

            data = {
                    'model_name': model_name,
                    'formset': formset,
                    'form': form_class,
                    'const': Const
            }

            print(data)
            return render(request, os.path.join('pms/pm/dispatch_create.html'), data)
    else:
        data = {'formset': formset,
                'const': Const}
        # print(data)
        return render(request, 'pms/pm/dispatch_create.html', data)
#
#
# @method_decorator(login_required, name='dispatch')
# class Risk(CreateView):
#     form_class = RiskModelFrom
#
#     template_name = "pms/pm/risk.html"
#     success_url = reverse_lazy('pms:select_model')
#
#     def form_valid(self, form):
#         # commit=FalseにしてPOSTされたデータを取得
#         postdata = form.save(commit=False)
#         # ユーザーのidを取得してモデルのuserフィールドに格納
#         postdata.user = self.request.user
#         # データをデータベースに登録
#         postdata.save()
#         # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
#         return super().form_valid(form)
#
#
# @method_decorator(login_required, name='dispatch')
# class Issue(CreateView):
#     form_class = IssueModelFrom
#
#     template_name = "pms/pm/risk.html"
#     success_url = reverse_lazy('pms:select_model')
#
#     def form_valid(self, form):
#         # commit=FalseにしてPOSTされたデータを取得
#         postdata = form.save(commit=False)
#         # ユーザーのidを取得してモデルのuserフィールドに格納
#         postdata.user = self.request.user
#         # データをデータベースに登録
#         postdata.save()
#         # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
#         return super().form_valid(form)
#
#
# @method_decorator(login_required, name='dispatch')
# class Scenario(CreateView):
#     form_class = ScenarioModelFrom
#
#     template_name = "pms/pm/risk.html"
#     success_url = reverse_lazy('pms:select_model')
#
#     def form_valid(self, form):
#         # commit=FalseにしてPOSTされたデータを取得
#         postdata = form.save(commit=False)
#         # ユーザーのidを取得してモデルのuserフィールドに格納
#         postdata.user = self.request.user
#         # データをデータベースに登録
#         postdata.save()
#         # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
#         return super().form_valid(form)
#
#
# @method_decorator(login_required, name='dispatch')
# class Bac(CreateView):
#     form_class = BacModelFrom
#
#     template_name = "pms/pm/risk.html"
#     success_url = reverse_lazy('pms:select_model')
#
#     def form_valid(self, form):
#         # commit=FalseにしてPOSTされたデータを取得
#         postdata = form.save(commit=False)
#         # ユーザーのidを取得してモデルのuserフィールドに格納
#         postdata.user = self.request.user
#         # データをデータベースに登録
#         postdata.save()
#         # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
#         return super().form_valid(form)
#
