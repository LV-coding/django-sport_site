# Generated by Django 4.0.4 on 2022-05-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabata', '0005_alter_training_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
