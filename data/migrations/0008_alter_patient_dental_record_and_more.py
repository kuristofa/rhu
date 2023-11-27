# Generated by Django 4.2.6 on 2023-10-11 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_alter_patient_address_alter_patient_dental_record_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='dental_record',
            field=models.FileField(default=None, upload_to='dental_record/'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='laboratory_record',
            field=models.FileField(default=None, upload_to='laboratory_record/'),
        ),
    ]