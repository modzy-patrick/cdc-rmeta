# Generated by Django 5.0.2 on 2024-04-01 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anonymouser', '0002_anonymizedmessage_dob_and_fn_and_ln_hash'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anonymizedmessage',
            old_name='hashlink',
            new_name='random_id',
        ),
        migrations.AddField(
            model_name='anonymizedmessage',
            name='patient_mobile_phone_number',
            field=models.CharField(blank=True, default='', max_length=36),
        ),
    ]
