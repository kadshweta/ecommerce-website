# Generated by Django 4.2.7 on 2023-12-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders_alter_contact_desc_alter_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=200),
        ),
    ]
