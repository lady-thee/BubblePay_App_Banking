# Generated by Django 4.2.2 on 2023-07-03 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers_app', '0004_account_account_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='pin',
        ),
    ]
