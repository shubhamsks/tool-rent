# Generated by Django 3.1.2 on 2020-10-12 05:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name of Tool')),
                ('description', models.TextField(verbose_name='Description')),
                ('quantity', models.IntegerField(blank=True, help_text='How many of these you have ?', null=True, verbose_name='Quantity')),
                ('cost', models.DecimalField(decimal_places=4, max_digits=10, verbose_name='Price of the Tool')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
