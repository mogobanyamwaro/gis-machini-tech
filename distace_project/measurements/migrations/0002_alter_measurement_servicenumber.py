# Generated by Django 3.2.6 on 2021-09-02 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='serviceNumber',
            field=models.IntegerField(),
        ),
    ]
