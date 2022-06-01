from django.db import models


class Stage(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|STAGE'
        verbose_name_plural = '|Mst|STAGE'

    stage = models.CharField(
        verbose_name='STAGE', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):

        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.stage
