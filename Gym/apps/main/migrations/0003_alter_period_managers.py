# Generated by Django 4.0.4 on 2022-05-04 09:04

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_majorgroups_alter_typepriod_options_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='period',
            managers=[
                ('coach', django.db.models.manager.Manager()),
            ],
        ),
    ]
