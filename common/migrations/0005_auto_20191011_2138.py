# Generated by Django 2.2.6 on 2019-10-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_remove_user_logged_in'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=300, unique=True),
        ),
    ]
