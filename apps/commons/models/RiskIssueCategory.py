from django.db import models


class RiskIssueCategory(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|分類（課題・リスク）'
        verbose_name_plural = '|Mst|分類（課題・リスク）'

    riskIssueCategory = models.CharField(
        verbose_name='分類（課題・リスク）', max_length=50, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.riskIssueCategory