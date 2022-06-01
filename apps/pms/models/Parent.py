from django.db import models
from apps.commons.models.Status import Status
from apps.accounts.models import CustomUser


class Parent(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Parent'
        verbose_name_plural = 'Parent'

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
        verbose_name='対象バージョン', max_length=100, default="")

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

    def __str__(self):
        return self.name