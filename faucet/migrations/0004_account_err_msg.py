# Generated by Django 2.0.7 on 2018-07-20 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faucet', '0003_auto_20180720_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='err_msg',
            field=models.TextField(null=True),
        ),
    ]
