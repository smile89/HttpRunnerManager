# Generated by Django 2.0.3 on 2018-06-08 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0004_auto_20180608_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debugtalk',
            options={'verbose_name': '驱动py文件'},
        ),
        migrations.AlterModelTable(
            name='debugtalk',
            table='DebugTalk',
        ),
    ]
