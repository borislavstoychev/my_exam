# Generated by Django 3.2.5 on 2021-07-07 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('pedicure', 'Pedicure'), ('manicure', 'Manicure'), ('else', 'Else')], default='else', max_length=10)),
                ('title', models.CharField(max_length=7)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images/nails')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sonq_nails.nail')),
            ],
        ),
    ]