# Generated by Django 3.0 on 2020-04-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmm', '0005_gymlocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='gymlocation',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='gymlocation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]