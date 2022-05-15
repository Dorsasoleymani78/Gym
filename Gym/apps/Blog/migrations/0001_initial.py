# Generated by Django 4.0.4 on 2022-04-15 14:03

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('content', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('img', models.ImageField(upload_to='images/blog', verbose_name='عکس')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='زمان ایجاد')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.major')),
            ],
            options={
                'verbose_name': 'وبلاگ',
                'verbose_name_plural': 'وبلاگ ها',
                'db_table': 'T_Blog',
            },
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.blog')),
            ],
        ),
    ]
