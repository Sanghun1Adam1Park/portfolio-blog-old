# Generated by Django 5.2 on 2025-04-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
