# Generated by Django 3.1 on 2020-11-30 18:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0003_auto_20201130_2346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
