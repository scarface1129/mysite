# Generated by Django 3.0 on 2020-05-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmm', '0009_gymlocation_my_date_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymlocation',
            name='my_date_field',
        ),
    ]
