# Generated by Django 4.2.16 on 2024-10-10 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='retailer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='retailer.retailer'),
        ),
    ]
