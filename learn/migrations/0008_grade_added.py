# Generated by Django 2.2.4 on 2019-08-16 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0007_auto_20190814_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='added',
            field=models.DateField(auto_now=True),
        ),
    ]
