# Generated by Django 5.1.3 on 2024-11-28 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_blacklistedtoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlacklistedToken',
        ),
    ]
