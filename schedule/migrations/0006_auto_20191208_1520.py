# Generated by Django 2.2.6 on 2019-12-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20191107_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mutation',
            old_name='rescheduled_end',
            new_name='added_end',
        ),
        migrations.RenameField(
            model_name='mutation',
            old_name='rescheduled_start',
            new_name='added_start',
        ),
        migrations.RemoveField(
            model_name='mutation',
            name='deleted',
        ),
        migrations.AddField(
            model_name='mutation',
            name='deleted_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mutation',
            name='deleted_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='room',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]