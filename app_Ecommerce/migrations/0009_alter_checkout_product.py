# Generated by Django 5.0.3 on 2024-06-09 06:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Ecommerce', '0008_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Ecommerce.product'),
        ),
    ]
