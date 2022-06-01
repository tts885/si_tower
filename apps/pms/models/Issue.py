from django.db import models
from django.forms.models import model_to_dict
from apps.commons.models.Status import Status
from apps.commons.models.Teams import Team,SubTeam
from apps.commons.models.RiskIssueCategory import RiskIssueCategory
from apps.commons.models.Phase import Phase
from apps.commons.models.ImpactScope import ImpactScope
from apps.commons.models.DelayReason import DelayReason
from apps.accounts.models import CustomUser


class Issue(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Issue'
        verbose_name_plural = 'Issue'

    name = models.CharField(
        verbose_name='題名', max_length=100, default="")

    status = models.ForeignKey(
        Status,
        verbose_name='ステータス',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='issue_status'
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
        related_name='issue_owner'
    )

    version = models.CharField(
        verbose_name='対象バージョン', blank=True, null=True, max_length=100, default="")

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

    remainingWorkTime = models.FloatField(
        verbose_name='残作業時間(h)',
        blank=True,
        null=True,
        default=0,
    )

    reviewOwner = models.ForeignKey(
        CustomUser,
        verbose_name='レビュー担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='reviewOwner'
    )

    remainingWorkTime = models.FloatField(
        verbose_name='残作業時間(h)',
        blank=True,
        null=True,
        default=0,
    )

    creater = models.ForeignKey(
        CustomUser,
        verbose_name='起票者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='creater'
    )

    createDate = models.DateField(
        verbose_name='起票日', blank=True, null=True,
    )

    contents = models.TextField(
        verbose_name='内容', blank=True, null=True,
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

    shareToPM = models.BooleanField(verbose_name='マネジメント共有')

    shareToClient = models.BooleanField(verbose_name='クライアント共有')

    clientConsideration = models.BooleanField(verbose_name='クライアント検討')

    dueDate = models.DateField(
        verbose_name='対応期限', blank=True, null=True,
    )

    completionCriteria = models.TextField(
        verbose_name='完了基準', blank=True, null=True,
    )

    riskIssueCategory = models.ForeignKey(
        RiskIssueCategory,
        verbose_name='分類（課題・リスク）',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    occurredPhase = models.ForeignKey(
        Phase,
        verbose_name='発生工程（課題・リスク）',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='occurredPhase'
    )

    solvePhase_Plan = models.ForeignKey(
        Phase,
        verbose_name='解決予定工程（課題・リスク）',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='solvePhase_Plan'
    )

    ownerClient = models.CharField(
        verbose_name='担当クライアント', blank=True, null=True, max_length=100, default="")

    impactScope = models.ForeignKey(
        ImpactScope,
        verbose_name='影響範囲',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    impactPhase = models.ForeignKey(
        Phase,
        verbose_name='影響工程',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='impactPhase'
    )

    solution = models.TextField(
        verbose_name='対応方針／状況', blank=True, null=True,
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

    def __str__(self):
        return self.name

    def to_dict(self):
        return model_to_dict(self)