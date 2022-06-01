from django.forms import ModelForm
from django import forms
from django.db import models
from apps.pms.models.Work import Work
from apps.pms.models.Deliverables import Deliverables
from apps.pms.models.Scenario import Scenario
from apps.pms.models.Issue import Issue
from apps.pms.models.Bac import Bac
from apps.pms.models.Risk import Risk
from apps.accounts.models import CustomUser
from apps.commons.models.Status import Status
from apps.pms.models.Parent import Parent
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.forms import TextInput, Textarea
from apps.pms.constant.common_cons import *


class AdvancedModelForm(ModelForm):
    """
    画面項目をReadonlyする共通class
    """

    def __init__(self, *arg, **kwrg):
        super(AdvancedModelForm, self).__init__(*arg, **kwrg)
        if hasattr(self, 'readonly'):
            for x in self.readonly:
                self.fields[x].widget.attrs['disabled'] = 'disabled'
                self.fields[x].widget.attrs['style'] = 'border:none'
                # self.fields[x].widget.attrs['style'] = 'background-color:#ffffff'
    #
    # def clean(self):
    #     data = super(AdvancedModelForm, self).clean()
    #     if hasattr(self, 'readonly'):
    #         for x in self.readonly:
    #             data[x] = getattr(self.instance, x)
    #     return data


class SelectModelFrom(forms.Form):
    """
    登録画面用フォーム
    """

    modelNames = []
    for i, model in enumerate(apps.all_models['pms']):
        print(apps.get_app_config('pms').get_model(model)._meta.verbose_name)

        modelNames.append(
            # [i, str(i + 1).zfill(2) + '|' + apps.get_app_config('pms').get_model(model)._meta.verbose_name])
            [i, apps.get_app_config('pms').get_model(model)._meta.verbose_name])

    selectForm = forms.ChoiceField(choices=modelNames)
    Status = forms.ModelChoiceField(label='', queryset=Status.objects.all(), required=False)


SelectModelFromSet = forms.formset_factory(SelectModelFrom, extra=1)


class WorkModelFrom(ModelForm):
    """
    登録画面用フォーム_Work
    """
    disp_name = forms.CharField(required=False)
    issue_id = forms.CharField(required=False)
    model_name = forms.CharField(required=False, initial=Const.MODEL_WORK)

    class Meta:
        model = Work
        fields = '__all__'


WorkModelFromSet = forms.formset_factory(WorkModelFrom, extra=1)


class BacModelFrom(ModelForm):
    """
    登録画面用フォーム_Bac
    """

    class Meta:
        model = Bac
        fields = '__all__'


class DeliverablesModelFrom(AdvancedModelForm):
    """
    登録画面用フォーム_Deliverables
    """
    # readonly = ('name',)
    class Meta:
        model = Deliverables
        fields = '__all__'


DeliverablesModelFromSet = forms.formset_factory(DeliverablesModelFrom, extra=1)


class ScenarioModelFrom(ModelForm):
    """
    登録画面用フォーム_Scenario
    """

    class Meta:
        model = Scenario
        fields = '__all__'


class IssueModelFrom(ModelForm):
    """
    登録画面用フォーム_Issue
    """
    disp_name = forms.CharField(required=False)
    issue_id = forms.CharField(required=False)
    model_name = forms.CharField(required=False, initial=Const.MODEL_ISSUE)

    class Meta:
        model = Issue
        fields = '__all__'


class RiskModelFrom(forms.ModelForm):
    """
    登録画面用フォーム
    """

    class Meta:
        model = Risk
        fields = '__all__'
