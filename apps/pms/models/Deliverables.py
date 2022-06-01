from django.db import models
from apps.commons.models.Status import Status
from apps.commons.models.Teams import Team, SubTeam
from apps.commons.models.DelayReason import DelayReason
from apps.pms.models.Parent import Parent
from apps.accounts.models import CustomUser
import reversion


@reversion.register()
class Deliverables(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Deliverables'
        verbose_name_plural = 'Deliverables'

    parent = models.ForeignKey(Parent, verbose_name='parent', related_name='parent',
                               null=True,blank=True,
                               on_delete=models.PROTECT, default="")

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

    reviewAssign = models.ForeignKey(
        CustomUser,
        verbose_name='レビュー担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='deliverablesReviewOwner'
    )

    deliverablesId = models.CharField(
        verbose_name='成果物ID', blank=True, null=True, max_length=100, default="")

    deliverablesName = models.CharField(
        verbose_name='成果物名称', blank=True, null=True, max_length=100, default="")

    team = models.ForeignKey(
        Team,
        verbose_name='チーム',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default=""
    )

    subTeam = models.ForeignKey(
        SubTeam,
        verbose_name='サブチーム',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default=""
    )

    delayReason = models.ForeignKey(
        DelayReason,
        verbose_name='遅延理由区分',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default=""
    )

    delayDescription = models.TextField(
        verbose_name='遅延理由詳細', blank=True, null=True,
    )

# ### Management Field ###
    system_user = models.ForeignKey(
        CustomUser,
        verbose_name='user',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='user',
        editable=False
    )

    timeStamp = models.DateTimeField('Record Time Stamp', auto_now_add=True)

    def __str__(self):
        return self.name