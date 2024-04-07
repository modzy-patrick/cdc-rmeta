# Generated by Django 5.0.2 on 2024-03-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0008_rename_next_shared_bscrypt_salt_jurisdiction_bscrypt_salt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiction',
            name='bscrypt_salt_rounds',
            field=models.PositiveSmallIntegerField(choices=[(11, '11'), (12, '12'), (13, '13')], default=12, help_text='Rounds or work factror for Bscrypt.'),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='bscrypt_salt_strategy',
            field=models.CharField(choices=[('shared', 'Shared'), ('unique', 'Unique')], default='shared', max_length=255),
        ),
    ]
