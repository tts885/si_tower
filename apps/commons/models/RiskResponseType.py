from django.db import models


class RiskResponseType(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|リスク対応タイプ'
        verbose_name_plural = '|Mst|リスク対応タイプ'

    riskResponseType = models.CharField(
        verbose_name='リスク対応タイプ', max_length=50, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.riskResponseType