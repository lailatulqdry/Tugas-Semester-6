# Generated by Django 5.0.3 on 2024-06-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Ecommerce', '0005_checkout'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]