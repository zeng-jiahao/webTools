# Generated by Django 2.2.24 on 2022-01-14 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_history'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='zjh_target',
            new_name='zjh_dic',
        ),
        migrations.RemoveField(
            model_name='history',
            name='zjh_method',
        ),
        migrations.RemoveField(
            model_name='history',
            name='zjh_result',
        ),
    ]
