from django.db import models
from apps.commons.models.Status import Status
from apps.commons.models.Teams import Team
from apps.commons.models.BacCategory import BacCategory


class Bac(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'BAC'
        verbose_name_plural = 'BAC'

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
        verbose_name='対象バージョン', blank=True, null=True, max_length=100, default="")

    parentTracker = models.CharField(
        verbose_name='親チケット', blank=True, null=True, max_length=100, default="")

    initialEstimate = models.FloatField(
        verbose_name='初期見積(h)',
        blank=True,
        null=True,
        default=0,
    )

    remainingEstimate = models.FloatField(
        verbose_name='残余見積(h)',
        blank=True,
        null=True,
        default=0,
    )

    team = models.ForeignKey(
        Team,
        verbose_name='チーム',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    bacCategory = models.ForeignKey(
        BacCategory,
        verbose_name='BAC種別',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    def __str__(self):
        return self.name