# Generated by Django 4.1.1 on 2022-09-13 11:38

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('spotapp', '0003_alter_drink_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='ingredients',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
