# Generated by Django 4.0.4 on 2022-05-05 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_period_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.major', verbose_name='نام رشته'),
        ),
    ]
