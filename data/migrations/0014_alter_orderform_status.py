# Generated by Django 4.2.6 on 2023-11-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_orderform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderform',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=100),
        ),
    ]