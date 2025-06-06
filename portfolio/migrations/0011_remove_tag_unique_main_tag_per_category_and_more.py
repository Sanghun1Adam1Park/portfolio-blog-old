# Generated by Django 5.2 on 2025-04-10 16:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_category_has_main_tag'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='tag',
            name='unique_main_tag_per_category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='has_main_tag',
        ),
        migrations.RemoveField(
            model_name='category',
            name='main_tag',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='is_main_tag',
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='main_tag', to='portfolio.category'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
