# Generated by Django 4.2.2 on 2023-07-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers_app', '0003_account_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
