from django.db import models
from utils.models import BaseModel

class Banner(BaseModel):
    images=models.ImageField(upload_to="slide",verbose_name="轮播图图片地址",null=True,blank=True,help_text="轮播图")
    name=models.CharField(max_length=20,verbose_name="轮播图名称")
    discrible=models.CharField(max_length=50,verbose_name="轮播图描述")
    banner_url=models.CharField(max_length=30,verbose_name="轮播图广告地址")
    class Meta:
        db_table="lbt"
        verbose_name="轮播图"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name


class MoblieList(BaseModel):
    images = models.ImageField(upload_to="mobile",verbose_name="手机图片地址",null=True,blank=True)
    name = models.CharField(max_length=30, verbose_name="手机图片名称")
    discrible = models.CharField(max_length=150, verbose_name="手机图片描述")
    banner_url = models.CharField(max_length=150, verbose_name="手机广告地址")
    class Meta:
        db_table="menu"
        verbose_name="菜单"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
