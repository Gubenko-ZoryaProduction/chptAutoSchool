# Generated by Django 3.0.3 on 2020-02-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chptautoschool', '0005_auto_20200214_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactphone',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
