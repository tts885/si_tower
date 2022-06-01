from django.db import models
import workdays
from apps.accounts.models import CustomUser
from apps.commons.models.Stage import Stage
from apps.commons.models.Status import Status


class Project(models.Model):
    class Meta:
        app_label = 'pms'
        verbose_name = 'Project'
        verbose_name_plural = 'Project'

    stage = models.ForeignKey(
        Stage,
        verbose_name='STAGE',
        on_delete=models.PROTECT
    )

    activity = models.CharField(
        verbose_name='Activity', max_length=100, default=""
    )

    task = models.CharField(
        verbose_name='Task', max_length=100, default=""
    )

    priority = (
        ('1', ''),
        ('2', 'Low'),
        ('3', 'High'),
        ('4', 'Normal'),
    )
    Priority = models.CharField('Priority', max_length=10, choices=priority, blank=True, null=True,   default='')

    newmodified = (
        ('1', ''),
        ('2', 'New'),
        ('3', 'Modified'),
        ('4', '-'),
    )
    NewModified = models.CharField('New/Modified', max_length=10, choices=newmodified, blank=True, null=True, default='')

    complexity = (
        ('1', ''),
        ('2', 'Simple'),
        ('3', 'Medium'),
        ('4', 'Complex'),
        ('5', 'Complex+'),
        ('6', 'Complex++'),
    )
    complexity = models.CharField('Complexity', max_length=10, choices=complexity, blank=True, null=True, default='')

    units = models.CharField('数量', max_length=10, blank=True, null=True,  default=1)

    estimate = models.CharField('Estimate', max_length=10,  blank=True, null=True, default='')

    scope = (
        ('1', 'InScope'),
        ('2', 'OutOfScope'),
    )
    scope = models.CharField('Scope', max_length=10, choices=scope, default='')


    status = models.ForeignKey(
        Status,
        verbose_name='Status',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    actualstartdate = models.DateField(
        verbose_name='実績開始日', blank=True, null=True,
    )

    actualenddate = models.DateField(
        verbose_name='実績終了日', blank=True, null=True,
    )

    start = models.DateField(
        verbose_name='予定開始日', blank=True, null=True,
    )

    duration = models.IntegerField('期間', blank=True, null=True, default=0)

    end = models.DateField(
        verbose_name='予定終了日', blank=True, null=True,
    )

    name = models.CharField(
        verbose_name='タスク名前', max_length=100, default="")

    progress = models.IntegerField('進捗率', blank=True, null=True, default=0)

    description = models.TextField(
        verbose_name='タスク詳細', blank=True, null=True,
    )

    code = models.CharField('タスクタイトル', max_length=10, blank=True, null=True, default="")

    level = models.IntegerField('WBSレベル', blank=True, null=True, default=0)

    # ####Gantt Control Model####
    ui_index = models.IntegerField('UI_INDEX', blank=True, null=True, default=0)

    progressByWorklog = models.BooleanField(verbose_name='progressByWorklog')

    type = models.CharField('type', max_length=10, blank=True, null=True, default="")

    typeId = models.CharField('typeId', max_length=10, blank=True, null=True, default="")

    gantt_status = models.CharField('ステータス', max_length=50, blank=True, null=True, default="")

    relevance = models.IntegerField('WBS依存', blank=True, null=True, default=0)

    depends = models.CharField('depends', max_length=10, blank=True, null=True, default="")

    startIsMilestone = models.BooleanField(verbose_name='マイルストーン設定（開始）')

    endIsMilestone = models.BooleanField(verbose_name='マイルストーン設定（終了）')

    collapsed = models.BooleanField(verbose_name='WBS折りたたみ設定')

    canWrite = models.BooleanField(verbose_name='書き込み可否', help_text='タスク直接権限設定該当項目はDurのみに対しての制御')

    canAdd = models.BooleanField(verbose_name='anAdd')

    canDelete = models.BooleanField(verbose_name='削除可否')

    canAddIssue = models.BooleanField(verbose_name='課題追加可否')

    assigs = models.ForeignKey(
        CustomUser,
        verbose_name='担当',
        on_delete=models.PROTECT,
        blank=True, null=True,
        default='',
    )

    hasChild = models.BooleanField(verbose_name='hasChild')

    def save(self, *args, **kwargs):
            self.duration = workdays.networkdays(self.start, self.end)
            super(Project, self).save(*args, **kwargs)
