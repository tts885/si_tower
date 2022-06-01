from django.db import models


class Status(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|ステータス'
        verbose_name_plural = '|Mst|ステータス'

    status = models.CharField(
        verbose_name='ステータス', max_length=20, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        return self.status