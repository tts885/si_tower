from django.db import models


class BusinessCategory(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|業務区分'
        verbose_name_plural = '|Mst|業務区分'

    businessCategory = models.CharField(
        verbose_name='業務区分', max_length=50, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.businessCategory