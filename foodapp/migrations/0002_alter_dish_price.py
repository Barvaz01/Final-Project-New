# Generated by Django 4.0.2 on 2022-07-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
