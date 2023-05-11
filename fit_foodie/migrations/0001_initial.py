# Generated by Django 3.1 on 2023-05-09 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'accounts',
            },
        ),
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('fid', models.IntegerField(primary_key=True, serialize=False)),
                ('fat', models.FloatField()),
                ('carbohydrates', models.FloatField()),
                ('cholesterol', models.FloatField()),
                ('protein', models.FloatField()),
                ('sodium', models.FloatField()),
                ('date', models.DateField(auto_now=True, verbose_name='Date')),
                ('fname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fit_foodie.accounts')),
            ],
        ),
    ]