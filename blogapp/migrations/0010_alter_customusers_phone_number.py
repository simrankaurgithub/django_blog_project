# Generated by Django 4.1.2 on 2022-11-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_customusers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
