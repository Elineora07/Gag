# Generated by Django 4.0.5 on 2022-06-30 12:04

from django.db import migrations, models
import gag.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to=gag.helpers.UploadTo('profile')),
        ),
    ]
