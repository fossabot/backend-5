# Generated by Django 2.2.6 on 2019-12-08 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0008_auto_20191208_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
