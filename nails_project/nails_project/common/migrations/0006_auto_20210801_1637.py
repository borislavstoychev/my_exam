# Generated by Django 3.2.5 on 2021-08-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
