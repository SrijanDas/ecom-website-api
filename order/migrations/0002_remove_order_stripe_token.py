# Generated by Django 3.2.3 on 2021-05-20 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='stripe_token',
        ),
    ]
