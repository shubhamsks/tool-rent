# Generated by Django 3.1.2 on 2020-12-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='payment_status',
            field=models.CharField(choices=[('not_completed', 'Not Completed'), ('partially_completed', 'Partially Completed'), ('completed', 'Completed')], max_length=50, null=True, verbose_name='Payment Status'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('ongoing', 'On Going'), ('expired', 'Expired')], max_length=50, null=True, verbose_name='Status'),
        ),
    ]
