# Generated by Django 3.0 on 2020-06-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmm', '0015_auto_20200621_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gymlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]