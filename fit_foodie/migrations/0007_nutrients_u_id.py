# Generated by Django 3.1 on 2023-05-10 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fit_foodie', '0006_auto_20230511_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrients',
            name='u_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fit_foodie.accounts'),
        ),
    ]
