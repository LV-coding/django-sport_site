# Generated by Django 4.0.4 on 2022-06-13 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabata', '0008_alter_article_title_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title_image',
        ),
    ]
