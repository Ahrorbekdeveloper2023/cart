# Generated by Django 5.0.6 on 2024-06-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_stock',
            field=models.BooleanField(default=True),
        ),
    ]
