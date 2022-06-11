# Generated by Django 3.2.13 on 2022-06-01 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baccategory',
            options={'verbose_name': '|Mst|BAC種別', 'verbose_name_plural': '|Mst|BAC種別'},
        ),
        migrations.AlterModelOptions(
            name='businesscategory',
            options={'verbose_name': '|Mst|業務区分', 'verbose_name_plural': '|Mst|業務区分'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '|Mst|CATEGORY', 'verbose_name_plural': '|Mst|CATEGORY'},
        ),
        migrations.AlterModelOptions(
            name='delayreason',
            options={'verbose_name': '|Mst|遅延理由区分', 'verbose_name_plural': '|Mst|遅延理由区分'},
        ),
        migrations.AlterModelOptions(
            name='functionalcategory',
            options={'verbose_name': '|Mst|機能区分', 'verbose_name_plural': '|Mst|機能区分'},
        ),
        migrations.AlterModelOptions(
            name='impactscope',
            options={'verbose_name': '|Mst|影響範囲', 'verbose_name_plural': '|Mst|影響範囲'},
        ),
        migrations.AlterModelOptions(
            name='phase',
            options={'verbose_name': '|Mst|工程', 'verbose_name_plural': '|Mst|工程'},
        ),
        migrations.AlterModelOptions(
            name='riskissuecategory',
            options={'verbose_name': '|Mst|分類（課題・リスク）', 'verbose_name_plural': '|Mst|分類（課題・リスク）'},
        ),
        migrations.AlterModelOptions(
            name='riskresponsetype',
            options={'verbose_name': '|Mst|リスク対応タイプ', 'verbose_name_plural': '|Mst|リスク対応タイプ'},
        ),
        migrations.AlterModelOptions(
            name='riskscope',
            options={'verbose_name': '|Mst|リスク種別', 'verbose_name_plural': '|Mst|リスク種別'},
        ),
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': '|Mst|STAGE', 'verbose_name_plural': '|Mst|STAGE'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': '|Mst|ステータス', 'verbose_name_plural': '|Mst|ステータス'},
        ),
        migrations.AlterModelOptions(
            name='subsystemcategory',
            options={'verbose_name': '|Mst|サブシステム区分', 'verbose_name_plural': '|Mst|サブシステム区分'},
        ),
        migrations.AlterModelOptions(
            name='subteam',
            options={'verbose_name': '|Mst|サブチーム', 'verbose_name_plural': '|Mst|サブチーム'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': '|Mst|チーム', 'verbose_name_plural': '|Mst|チーム'},
        ),
        migrations.AlterModelOptions(
            name='testtype',
            options={'verbose_name': '|Mst|テスト種別', 'verbose_name_plural': '|Mst|テスト種別'},
        ),
        migrations.AlterModelOptions(
            name='worksite',
            options={'verbose_name': '|Mst|WORK SITE', 'verbose_name_plural': '|Mst|WORK SITE'},
        ),
        migrations.AlterModelOptions(
            name='worktype',
            options={'verbose_name': '|Mst|作業種別', 'verbose_name_plural': '|Mst|作業種別'},
        ),
    ]
