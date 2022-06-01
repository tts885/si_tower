from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.pms.forms import DeliverablesModelFromSet,DeliverablesModelFrom
from apps.pms.forms import SelectModelFromSet,SelectModelFrom
from apps.pms.forms import WorkModelFrom,WorkModelFromSet
from apps.pms.forms import IssueModelFrom
from apps.pms.forms import ScenarioModelFrom
from apps.pms.forms import BacModelFrom
from apps.pms.forms import RiskModelFrom
from apps.pms.constant.common_cons import *


@login_required()
def initial_view(request):

    if request.method == 'GET':
        select_model_form = SelectModelFrom
        context = {'select_model_form': select_model_form, 'const': Const}
        return render(request, 'pms/pm/dispatch_search.html', context)

    elif request.method == 'POST':
        select_model_form = SelectModelFrom(request.POST)
        if not select_model_form.is_valid():  # バリデーションを行う
            context = {'select_model_form': select_model_form}
            return render(request, Const.PM_SEARCH_URL, context)

        selected_model = select_model_form.cleaned_data[Const.SESSION_SELECT_FORM]
        model_name = select_model_form.modelNames[int(selected_model)][1]

        request.session[Const.SESSION_SELECT_FORM] = selected_model
        request.session[Const.SESSION_MODEL_NAME] = model_name

        if model_name == Const.MODEL_PROJECT:
            search_form = WorkModelFrom

        elif model_name == Const.MODEL_TRACKER:
            search_form = WorkModelFrom

        elif model_name == Const.MODEL_DELIVERABLES:
            search_form = DeliverablesModelFrom

        elif model_name == Const.MODEL_PARENT:
            search_form = ParentModelFromSet

        elif model_name == Const.MODEL_WORK:
            search_form = WorkModelFrom

        elif model_name == Const.MODEL_SCENARIO:
            search_form = ScenarioModelFrom

        elif model_name == Const.MODEL_BAC:
            search_form = BacModelFrom

        elif model_name == Const.MODEL_ISSUE:
            search_form = IssueModelFrom

        elif model_name == Const.MODEL_RISK:
            search_form = RiskModelFrom

        context = {
                'model_name': model_name,
                'select_model_form': select_model_form,
                'search_form': search_form,
                'const': Const
        }

        return render(request, 'pms/pm/dispatch_search.html', context)

    else:
        return HttpResponse('不正なメソッドです', status=500)