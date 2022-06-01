from django.db import models


class ImpactScope(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|影響範囲'
        verbose_name_plural = '|Mst|影響範囲'

    impactScope = models.CharField(
        verbose_name='影響範囲', max_length=20
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        return self.impactScope
