# Generated by Django 3.0 on 2020-06-06 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_activation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_key',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
