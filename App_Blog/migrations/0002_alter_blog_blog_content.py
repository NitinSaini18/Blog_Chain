# Generated by Django 3.2.8 on 2021-10-12 19:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
