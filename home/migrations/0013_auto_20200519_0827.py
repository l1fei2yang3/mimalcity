# Generated by Django 2.0.6 on 2020-05-19 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200518_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adslist',
            old_name='imges',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='adslist',
            old_name='imges_url',
            new_name='images_url',
        ),
    ]
