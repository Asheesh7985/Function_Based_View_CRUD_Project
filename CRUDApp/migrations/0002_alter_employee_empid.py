# Generated by Django 5.0.7 on 2024-07-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUDApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empID',
            field=models.CharField(max_length=70),
        ),
    ]
