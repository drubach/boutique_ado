# Generated by Django 3.2 on 2022-02-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
