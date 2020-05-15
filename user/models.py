from django.db import models

# Create your models here.
#因为用了auth 故需要在settings文件当中配置 AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile=models.CharField(max_length=20,null=True,blank=True)
    class Meta:
        db_table="user"
        verbose_name="用戶表"
        verbose_name_plural=verbose_name
