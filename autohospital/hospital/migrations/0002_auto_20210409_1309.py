# Generated by Django 3.1.1 on 2021-04-09 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor_model',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='patient_model',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
