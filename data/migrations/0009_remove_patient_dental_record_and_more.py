# Generated by Django 4.2.6 on 2023-10-11 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_alter_patient_dental_record_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='dental_record',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='laboratory_record',
        ),
        migrations.AlterField(
            model_name='patient',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]