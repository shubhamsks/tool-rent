# Generated by Django 3.1.2 on 2020-11-29 10:34

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img/default_profile.jpg', upload_to=users.models.upload_profile, verbose_name='User Profile Pic'),
        ),
    ]
