# Generated by Django 2.0.4 on 2018-09-18 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_team', '0004_auto_20180816_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='team',
            field=models.CharField(choices=[('Core Team', 'Core'), ('Advisor', 'Advisor'), ('Partner', 'Partner')], max_length=40),
        ),
    ]
