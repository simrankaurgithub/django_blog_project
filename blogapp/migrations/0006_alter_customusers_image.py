# Generated by Django 4.1.2 on 2022-11-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_customusers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
