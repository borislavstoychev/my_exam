# Generated by Django 3.2.5 on 2021-08-01 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sonq_nails', '0004_rename_pet_like_nails'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nails',
            name='title',
        ),
        migrations.AddField(
            model_name='nails',
            name='feedback',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
