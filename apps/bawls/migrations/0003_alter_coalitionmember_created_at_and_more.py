# Generated by Django 4.2.16 on 2025-04-10 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bawls', '0002_alter_coalitionmember_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coalitionmember',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable='false'),
        ),
        migrations.AlterField(
            model_name='galleryitem',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable='false'),
        ),
    ]
