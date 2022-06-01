from django.db import models


class Category(models.Model):
    class Meta:
        app_label = 'commons'
        verbose_name = '|Mst|CATEGORY'
        verbose_name_plural = '|Mst|CATEGORY'

    title = models.CharField(
        verbose_name='CATEGORY', max_length=20
    )

    comments = models.TextField(
        verbose_name='COMMENTS', blank=True, null=True, default=''
    )

    def __str__(self):
        return self.title
