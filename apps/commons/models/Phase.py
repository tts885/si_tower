from django.db import models


class Phase(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|工程'
        verbose_name_plural = '|Mst|工程'

    phase = models.CharField(
        verbose_name='工程', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.phase