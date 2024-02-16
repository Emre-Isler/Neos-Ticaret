# Generated by Django 5.0.2 on 2024-02-15 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_favorites_alter_product_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piece', models.IntegerField(default=1, verbose_name='Sepete eknen ürünün adeti')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5, verbose_name='Toplam Fiyat')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Alıcı')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Eklenen Ürün')),
            ],
            options={
                'verbose_name': 'Sepetteki Ürün',
                'verbose_name_plural': 'Sepetteki Ürünler',
            },
        ),
    ]
