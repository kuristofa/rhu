# Generated by Django 3.2.16 on 2023-11-14 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20231114_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drug',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='drug',
            name='unit_price',
        ),
    ]
