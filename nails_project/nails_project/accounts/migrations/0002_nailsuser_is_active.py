# Generated by Django 3.2.5 on 2021-08-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nailsuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]