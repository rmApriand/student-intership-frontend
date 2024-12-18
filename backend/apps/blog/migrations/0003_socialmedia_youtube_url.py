# Generated by Django 5.1.4 on 2024-12-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_navbar_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='youtube_url',
            field=models.URLField(blank=True, max_length=512, null=True, verbose_name='Youtube URL'),
        ),
    ]
