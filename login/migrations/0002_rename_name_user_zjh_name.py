# Generated by Django 4.0 on 2022-01-12 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='zjh_name',
        ),
    ]
