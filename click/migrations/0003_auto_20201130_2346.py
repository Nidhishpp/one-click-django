# Generated by Django 3.1 on 2020-11-30 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('click', '0002_auto_20201129_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='SOME STRING', upload_to='category'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='SOME STRING', upload_to='service'),
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('booking_time', models.TextField()),
                ('location', models.TextField()),
                ('phn', models.BigIntegerField()),
                ('status', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='click.service')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
