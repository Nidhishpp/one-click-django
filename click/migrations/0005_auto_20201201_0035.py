# Generated by Django 3.1 on 2020-11-30 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('click', '0004_auto_20201201_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('staff assigned', 'staff assigned'), ('In progress', 'In progress')], max_length=256),
        ),
    ]
