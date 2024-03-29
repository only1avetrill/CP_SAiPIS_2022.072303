# Generated by Django 4.0.4 on 2022-05-26 14:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_ad_address_index_alter_ad_area_alter_ad_budget_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MethodMarks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark1', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка 1')),
                ('mark2', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка 2')),
                ('mark3', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка 3')),
            ],
            options={
                'verbose_name': 'Экспертная оценка',
                'verbose_name_plural': 'Экспертные оценки',
            },
        ),
        migrations.CreateModel(
            name='MonkeyIsVoted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('is_voted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MethodResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='ExecutorRank',
        ),
    ]
