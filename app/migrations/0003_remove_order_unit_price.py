# Generated by Django 3.2.12 on 2022-03-15 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='unit_price',
        ),
    ]
