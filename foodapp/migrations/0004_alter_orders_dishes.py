# Generated by Django 4.0.2 on 2022-07-16 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0003_alter_dish_category_alter_orders_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='dishes',
            field=models.ManyToManyField(blank=True, to='foodapp.Dish'),
        ),
    ]