from django.db import models


class SubSystemCategory(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|サブシステム区分'
        verbose_name_plural = '|Mst|サブシステム区分'

    subSystemCategory = models.CharField(
        verbose_name='サブシステム区分', max_length=50, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.subSystemCategory