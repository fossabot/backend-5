# Generated by Django 2.2.6 on 2019-10-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('common', '0009_user_uuid'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SettingDefition',
            new_name='SettingDefinition',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uuid',
        ),
    ]
