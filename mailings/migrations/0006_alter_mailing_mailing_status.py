# Generated by Django 4.2 on 2024-02-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0005_mailing_mailing_status_mailing_mailing_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='mailing_status',
            field=models.IntegerField(default=1, max_length=1),
        ),
    ]
