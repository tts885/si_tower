from django.db import models


class DelayReason(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|遅延理由区分'
        verbose_name_plural = '|Mst|遅延理由区分'

    delayReason = models.CharField(
        verbose_name='遅延理由区分', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.delayReason