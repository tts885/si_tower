from django.db import models


class TestType(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|テスト種別'
        verbose_name_plural = '|Mst|テスト種別'

    testType = models.CharField(
        verbose_name='テスト種別', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.testType