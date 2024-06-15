# Generated by Django 5.0.6 on 2024-06-14 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cotegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField()),
                ('discription', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='product_image')),
                ('cotegory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='cart.cotegory')),
            ],
        ),
    ]
