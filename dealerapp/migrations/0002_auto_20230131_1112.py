# Generated by Django 3.1 on 2023-01-31 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panchayat',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
