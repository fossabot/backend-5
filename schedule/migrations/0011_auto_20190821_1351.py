# Generated by Django 2.2.4 on 2019-08-21 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0014_auto_20190818_1220'),
        ('schedule', '0010_auto_20190817_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='event',
        ),
        migrations.AddField(
            model_name='exercise',
            name='subject',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='common.Subject'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='due',
            field=models.DateTimeField(),
        ),
    ]