# Generated by Django 2.0.6 on 2020-05-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200518_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='排序')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否上架')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('create_time', models.DateField(auto_now_add=True, null=True, verbose_name='上传时间')),
                ('updated_time', models.DateField(auto_now=True, null=True, verbose_name='更新时间')),
                ('imges', models.ImageField(blank=True, help_text='广告位上传图片', null=True, upload_to='ads', verbose_name='广告位上传图片')),
                ('imges_url', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': '广告表',
                'db_table': 'ads',
                'verbose_name_plural': '广告表',
            },
        ),
    ]
