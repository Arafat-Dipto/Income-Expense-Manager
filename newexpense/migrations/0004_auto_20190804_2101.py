# Generated by Django 2.2.4 on 2019-08-04 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newexpense', '0003_auto_20190804_2024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='user',
            new_name='userName',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='user',
            new_name='userName',
        ),
    ]
