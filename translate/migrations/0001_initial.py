# Generated by Django 5.0.1 on 2024-01-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('first_name_en_us', models.CharField(max_length=30, null=True, verbose_name='First Name')),
                ('first_name_uz', models.CharField(max_length=30, null=True, verbose_name='First Name')),
                ('first_name_ru', models.CharField(max_length=30, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('last_name_en_us', models.CharField(max_length=30, null=True, verbose_name='Last Name')),
                ('last_name_uz', models.CharField(max_length=30, null=True, verbose_name='Last Name')),
                ('last_name_ru', models.CharField(max_length=30, null=True, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
            },
        ),
    ]
