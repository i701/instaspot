# Generated by Django 4.1.1 on 2022-09-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotapp', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
