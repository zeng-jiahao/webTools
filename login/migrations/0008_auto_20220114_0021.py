# Generated by Django 2.2.24 on 2022-01-14 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20220114_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='history',
            options={'ordering': ['c_time'], 'verbose_name': '用户', 'verbose_name_plural': '用户'},
        ),
    ]