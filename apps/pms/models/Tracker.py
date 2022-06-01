from django.db import models
from apps.commons.models.Status import Status
from apps.accounts.models import CustomUser
from apps.commons.models.Teams import Team, SubTeam


# 865_Lv1
# 題名
# 説明
# ステータス
# 対象バージョン
# EV自動計上する


class Tracker(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Tracker'
        verbose_name_plural = 'Tracker'

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

    version = models.CharField(
        verbose_name='対象バージョン', max_length=100, default="")

    autoEvCount = models.BooleanField(verbose_name='EV自動計上する')

    parentTracker = models.TextField(
        verbose_name='親チケット', blank=True, null=True,
    )

    assigs = models.ForeignKey(
        CustomUser,
        verbose_name='担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='assigs'
    )

    assigsReview = models.ForeignKey(
        CustomUser,
        verbose_name='レビュー担当者',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
        related_name='assigsReview'
    )

    deliverablesId = models.TextField(
        verbose_name='成果物ID', blank=True, null=True,
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

    def __str__(self):
        return self.name