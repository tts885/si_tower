from django.db import models
from apps.commons.models.Status import Status
from apps.commons.models.Teams import Team, SubTeam
from apps.commons.models.TestType import TestType
from apps.commons.models.SubSystemCategory import SubSystemCategory
from apps.commons.models.BusinessCategory import BusinessCategory
from apps.commons.models.FunctionalCategory import FunctionalCategory
from apps.accounts.models import CustomUser


class Scenario(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Scenario'
        verbose_name_plural = 'Scenario'

    name = models.CharField(
        verbose_name='題名', max_length=100, default="")

    description = models.TextField(
        verbose_name='説明', blank=True, null=True,
    )

    status = models.ForeignKey(
        Status,
        verbose_name='ステータス',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    owner = models.ForeignKey(
        CustomUser,
        verbose_name='担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    version = models.CharField(
        verbose_name='対象バージョン', blank=True, null=True, max_length=100, default="")

    parentTracker = models.CharField(
        verbose_name='親チケット', blank=True, null=True, max_length=100, default="")

    planStartDate = models.DateField(
        verbose_name='予定開始日', blank=True, null=True,
    )

    planEndDate = models.DateField(
        verbose_name='予定終了日', blank=True, null=True,
    )

    actualStartDate = models.DateField(
        verbose_name='実績開始日', blank=True, null=True,
    )

    actualEndDate = models.DateField(
        verbose_name='実績終了日', blank=True, null=True,
    )

    estimate = models.FloatField(
        verbose_name='予定工数',
        blank=True,
        null=True,
        default=0,
    )

    deliverablesId = models.CharField(
        verbose_name='成果物ID', blank=True, null=True, max_length=100, default="")

    team = models.ForeignKey(
        Team,
        verbose_name='チーム',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    subTeam = models.ForeignKey(
        SubTeam,
        verbose_name='サブチーム',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    totalTestItems = models.CharField('テスト項目総数', max_length=12, default=0)

    completedTestItems = models.CharField('テスト項目完了数', max_length=12, default=0)

    testType = models.ForeignKey(
        TestType,
        verbose_name='テスト工程',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',)

    subSystemCategory = models.ForeignKey(
        SubSystemCategory,
        verbose_name='サブシステム区分',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    businessCategory = models.ForeignKey(
        BusinessCategory,
        verbose_name='業務区分',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    functionalCategory = models.ForeignKey(
        FunctionalCategory,
        verbose_name='機能区分',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    def __str__(self):
        return self.name
