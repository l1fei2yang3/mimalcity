# Generated by Django 2.0.6 on 2020-05-18 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200518_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='middlenavheadermobile',
            old_name='midhear',
            new_name='midheader',
        ),
    ]
