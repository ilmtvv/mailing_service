# Generated by Django 4.2 on 2024-03-03 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_alter_log_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='mailing',
            field=models.CharField(default='test', max_length=25),
        ),
    ]
