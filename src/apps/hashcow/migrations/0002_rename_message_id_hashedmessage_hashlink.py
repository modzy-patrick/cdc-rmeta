# Generated by Django 5.0.2 on 2024-03-27 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hashcow', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashedmessage',
            old_name='message_id',
            new_name='hashlink',
        ),
    ]
