# Generated by Django 2.2.4 on 2019-08-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0018_auto_20190822_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='tests', to='learn.Note'),
        ),
    ]
