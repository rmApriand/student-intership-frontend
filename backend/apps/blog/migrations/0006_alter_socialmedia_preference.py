# Generated by Django 5.1.4 on 2024-12-18 15:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_socialmedia_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='preference',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social_medias', to='blog.preference', verbose_name='Preference'),
        ),
    ]
