# Generated by Django 3.2.12 on 2022-03-24 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
    ]
