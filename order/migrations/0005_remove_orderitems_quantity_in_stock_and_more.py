# Generated by Django 4.0.3 on 2022-03-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20220325_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='quantity_in_stock',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_in_stock',
            field=models.IntegerField(default=0),
        ),
    ]
