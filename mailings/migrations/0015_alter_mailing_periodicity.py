# Generated by Django 4.2 on 2024-02-25 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailings', '0014_alter_mailing_mailing_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='periodicity',
            field=models.CharField(choices=[('D', 'Day'), ('W', 'Week'), ('M', 'Month')], max_length=15),
        ),
    ]
