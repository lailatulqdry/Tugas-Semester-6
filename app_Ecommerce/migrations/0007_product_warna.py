# Generated by Django 5.0.3 on 2024-06-09 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Ecommerce', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warna',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
