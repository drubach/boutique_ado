# Generated by Django 3.2 on 2022-02-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200211_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
