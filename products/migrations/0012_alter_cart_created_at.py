# Generated by Django 5.0.2 on 2024-02-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Eklenen Tarih'),
        ),
    ]