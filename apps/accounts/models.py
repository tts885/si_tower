from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    UserModelを継承するモデル
    '''
    pass

    Invitation_code = models.CharField(
        verbose_name='招待コード',help_text='招待コードを入力ください。', max_length=100, default="")