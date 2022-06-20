from django.db import models
from model_utils import FieldTracker
from apps.commons.models.Status import Status
from apps.commons.models.Teams import Team, SubTeam
from apps.commons.models.DelayReason import DelayReason
from apps.commons.models.WorkType import WorkType
from apps.commons.models.WorkSite import WorkSite
from apps.pms.models.Issue import Issue
from apps.accounts.models import CustomUser
import reversion


@reversion.register()
class Work(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Work'
        verbose_name_plural = 'Work'

    issue = models.ManyToManyField(Issue, blank=True, default="")

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

    priority = (
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Normal'),
    )
    Priority = models.CharField('優先度', max_length=10, choices=priority, default='')

    owner = models.ForeignKey(
        CustomUser,
        verbose_name='担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    version = models.CharField(
        verbose_name='対象バージョン', max_length=100, default="")

    parentTracker = models.CharField(
        verbose_name='親チケット',  max_length=100, default="")

    planStartDate = models.DateField(
        verbose_name='予定開始日', blank=True, null=True,
    )

    planEndDate = models.DateTimeField(
        verbose_name='予定終了日', blank=True, null=True,
    )

    actualStartDate = models.DateField(
        verbose_name='実績開始日', blank=True, null=True,
    )

    actualEndDate = models.DateTimeField(
        verbose_name='実績終了日', blank=True, null=True,
    )

    estimate = models.FloatField(
        verbose_name='予定工数',
        blank=True,
        null=True,
        default=0,
    )

    reviewAssign = models.ForeignKey(
        CustomUser,
        verbose_name='レビュー担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='reviewAssign'
    )

    remainingWorkTime = models.FloatField(
        verbose_name='残作業時間(h)',
        blank=True,
        null=True,
        default=0,
    )

    acceptanceCriteria = models.TextField(
        verbose_name='受け入れ基準', blank=True, null=True,
    )

    workType = models.ForeignKey(
        WorkType,
        verbose_name='作業種別',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

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

    delayReason = models.ForeignKey(
        DelayReason,
        verbose_name='遅延理由区分',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    delayDescription = models.TextField(
        verbose_name='遅延理由詳細', blank=True, null=True,
    )

    workSite = models.ForeignKey(
        WorkSite,
        verbose_name='WorkSite',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    tracker = FieldTracker()

    def __str__(self):
        return self.name