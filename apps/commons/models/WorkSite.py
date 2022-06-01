from django.db import models


class WorkSite(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|WORK SITE'
        verbose_name_plural = '|Mst|WORK SITE'

    workSite = models.CharField(
        verbose_name='WorkSite', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.workSite