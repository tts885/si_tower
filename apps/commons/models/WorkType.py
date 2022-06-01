from django.db import models

class WorkType(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|作業種別'
        verbose_name_plural = '|Mst|作業種別'

    workType = models.CharField(
        verbose_name='作業種別', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.workType