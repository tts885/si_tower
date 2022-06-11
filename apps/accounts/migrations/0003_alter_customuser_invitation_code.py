# Generated by Django 3.2.13 on 2022-06-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_invitation_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Invitation_code',
            field=models.CharField(default='', help_text='招待コードを入力ください。', max_length=100, verbose_name='招待コード'),
        ),
    ]
