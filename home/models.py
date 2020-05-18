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

class MiddleNavHeader(BaseModel):
    title=models.CharField(max_length=20,verbose_name="导航栏标题名称")
    class Meta:
        db_table="mnav"
        verbose_name="中部导航栏标题"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title

class MiddleNavHeaderMobile(BaseModel):
    images=models.ImageField(upload_to="nav-img",verbose_name="中部导航栏图片",null=True,blank=True)
    title=models.CharField(max_length=20,verbose_name="中部导航栏标题")
    price=models.IntegerField(verbose_name="中部导航栏价格")
    midheader=models.ForeignKey("MiddleNavHeader",on_delete=models.CASCADE,verbose_name="外键关联中部标题",related_name="mid_header")
    images_url=models.CharField(max_length=120,null=True,blank=True)
    class Meta:
        db_table="mnav_header"
        verbose_name="中部导航栏数据"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title


class AdsList(BaseModel):
    imges=models.ImageField(upload_to="ads",verbose_name="广告位上传图片",null=True,blank=True,help_text="广告位上传图片")
    imges_url=models.CharField(max_length=100)
    class Meta:
        db_table="ads"
        verbose_name="广告表"
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.imges_url



