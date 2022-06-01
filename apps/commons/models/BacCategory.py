from django.db import models


class BacCategory(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|BAC種別'
        verbose_name_plural = '|Mst|BAC種別'

    bacCategory = models.CharField(
        verbose_name='BAC種別', max_length=50, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.bacCategory