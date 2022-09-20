# Generated by Django 3.2.5 on 2021-07-24 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
            ],
            options={
                'verbose_name': 'UserN',
                'verbose_name_plural': 'UserNs',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ПродуКТ')),
                ('description', models.CharField(blank=True, max_length=255, verbose_name='описание')),
                ('quality', models.CharField(default='quality NONE', max_length=100, verbose_name='каЧестВо')),
                ('usern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test13.usern', verbose_name='ЮЗЕР')),
            ],
            options={
                'verbose_name': 'ПроДукТ',
                'verbose_name_plural': 'ПроДукТы',
            },
        ),
    ]
