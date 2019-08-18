# Generated by Django 2.2.4 on 2019-08-14 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_note_filepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='actual',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "The progress can't be a negative value"), django.core.validators.MaxValueValidator(1, 'The progress should be a value between 0 and 1')]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='expected',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "The progress can't be a negative value"), django.core.validators.MaxValueValidator(1, 'The progress should be a value between 0 and 1')]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='goal',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, "The progress can't be a negative value"), django.core.validators.MaxValueValidator(1, 'The progress should be a value between 0 and 1')]),
        ),
        migrations.AlterField(
            model_name='grade',
            name='weight',
            field=models.FloatField(default=1),
        ),
    ]