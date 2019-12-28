# Generated by Django 2.2.6 on 2019-12-28 17:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20191221_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='goal',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, "This can't be greater than 1")]),
        ),
    ]
