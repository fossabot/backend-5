# Generated by Django 2.2.6 on 2019-12-15 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0012_auto_20191212_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='obtained_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='obtained',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "This can't be a negative value"), django.core.validators.MaxValueValidator(1, 'This should be a value between 0 and 1')], verbose_name='Obtained grade'),
        ),
    ]