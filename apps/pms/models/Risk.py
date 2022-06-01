from django.db import models
from apps.commons.models.Status import Status
from apps.commons.models.Teams import Team,SubTeam
from apps.commons.models.RiskIssueCategory import RiskIssueCategory
from apps.commons.models.Phase import Phase
from apps.commons.models.ImpactScope import ImpactScope
from apps.commons.models.DelayReason import DelayReason
from apps.commons.models.RiskScope import RiskScope
from apps.commons.models.RiskResponseType import RiskResponseType
from apps.accounts.models import CustomUser
from apps.pms.models.Work import Work


class Risk(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Risk'
        verbose_name_plural = 'Risk'

    # work = models.ManyToManyField(Work, blank=True, default="")

    name = models.CharField(
        verbose_name='題名', max_length=100, default="")

    status = models.ForeignKey(
        Status,
        verbose_name='ステータス',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_status'
    )

    owner = models.ForeignKey(
        CustomUser,
        verbose_name='担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_owner'
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

    creater = models.ForeignKey(
        CustomUser,
        verbose_name='起票者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_creater'
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
        related_name='risk_team'
    )

    subTeam = models.ForeignKey(
        SubTeam,
        verbose_name='サブチーム',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_subteam'
    )

    riskScope = models.ForeignKey(
        RiskScope,
        verbose_name='リスク種別',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_Scope'
    )

    shareToClient = models.BooleanField(verbose_name='クライアント共有')

    dueDate = models.DateField(
        verbose_name='対応期限', blank=True, null=True,
    )

    planReviewDate = models.DateField(
        verbose_name='次回レビュー日', blank=True, null=True,
    )

    riskExtinctionPlanDate = models.DateField(
        verbose_name='リスク消滅予定日', blank=True, null=True,
    )

    completionCriteria = models.TextField(
        verbose_name='リスク消滅基準', blank=True, null=True,
    )

    riskResponseType = models.ForeignKey(
        RiskResponseType,
        verbose_name='リスク対応タイプ',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_ResponseType'

    )

    costImpactOfRisk = models.TextField(
        verbose_name='リスクによるコスト影響', blank=True, null=True,
    )

    costs = models.FloatField(
        verbose_name='リスク対応に必要なコスト',
        blank=True,
        null=True,
        default=0,
    )

    contingencyPlan = models.TextField(
        verbose_name='リスク発現時のコンティンジェンシープラン', blank=True, null=True,
    )

    riskManifestationDate = models.DateField(
        verbose_name='リスク顕在化日', blank=True, null=True,
    )

    riskExtinctionDate = models.DateField(
        verbose_name='リスク消滅日', blank=True, null=True,
    )

    riskIssueCategory = models.ForeignKey(
        RiskIssueCategory,
        verbose_name='分類（課題・リスク）',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='riskCategory'
    )

    occurredPhase = models.ForeignKey(
        Phase,
        verbose_name='発生工程（課題・リスク）',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_occurredPhase'
    )

    solvePhase_Plan = models.ForeignKey(
        Phase,
        verbose_name='解決予定工程（課題・リスク）',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_solvePhase_Plan'
    )

    occurrenceProbability = (
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Normal'),
    )

    occurrenceProbability = models.CharField('発生確率', max_length=10, choices=occurrenceProbability, default='')

    impact = (
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Normal'),
    )

    impact = models.CharField('影響度', max_length=10, choices=impact , default='')

    impactScope = models.ForeignKey(
        ImpactScope,
        verbose_name='影響範囲',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='risk_impactScope'
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
        related_name='risk_delayReason'
    )

    delayDescription = models.TextField(
        verbose_name='遅延理由詳細', blank=True, null=True,
    )

    def __str__(self):
        return self.name