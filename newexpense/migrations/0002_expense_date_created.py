# Generated by Django 2.2.4 on 2019-08-04 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newexpense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]