# Generated by Django 4.2 on 2024-02-25 02:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0013_alter_mailing_mailing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mailing_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
