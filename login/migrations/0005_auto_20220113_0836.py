# Generated by Django 2.2.24 on 2022-01-13 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20220112_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='email',
            new_name='zjh_email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='zjh_password',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='sex',
            new_name='zjh_sex',
        ),
    ]
