# Generated by Django 5.0.6 on 2024-08-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
