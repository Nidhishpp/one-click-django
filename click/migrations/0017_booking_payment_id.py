# Generated by Django 3.1.4 on 2020-12-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0016_auto_20201214_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='payment_id',
            field=models.TextField(default='nil'),
        ),
    ]