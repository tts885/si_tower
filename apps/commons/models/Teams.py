from django.db import models


class Team(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|チーム'
        verbose_name_plural = '|Mst|チーム'

    team = models.CharField(
        verbose_name='チーム', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.team


class SubTeam(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|サブチーム'
        verbose_name_plural = '|Mst|サブチーム'

    subTeam = models.CharField(
        verbose_name='サブチーム', max_length=30, default=''
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        """
        オブジェクトを文字列に変換して返す

        Returns(str):カテゴリ名
        """

        return self.subTeam
