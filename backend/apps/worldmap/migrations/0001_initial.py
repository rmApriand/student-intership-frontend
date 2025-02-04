# Generated by Django 5.1.4 on 2024-12-17 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=8, unique=True)),
                ('code3', models.CharField(max_length=8, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('tld', models.CharField(max_length=8)),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Country',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Province',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Regency',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='worldmap.province')),
            ],
            options={
                'verbose_name': 'Regency',
                'verbose_name_plural': 'Regency',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('regency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='worldmap.regency')),
            ],
            options={
                'verbose_name': 'District',
                'verbose_name_plural': 'District',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='worldmap.district')),
            ],
            options={
                'verbose_name': 'Village',
                'verbose_name_plural': 'Village',
                'ordering': ['name'],
            },
        ),
    ]
