# Generated by Django 2.2.4 on 2019-08-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0019_auto_20190823_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='due',
            field=models.DateField(),
        ),
    ]