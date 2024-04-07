# Generated by Django 5.0.2 on 2024-03-08 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0011_alter_sourcesoftware_vendor_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together={('partner', 'source_system', 'cdc_receiving_system')},
        ),
        migrations.AlterField(
            model_name='sourcesoftware',
            name='version',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.RemoveField(
            model_name='connection',
            name='code',
        ),
        migrations.RemoveField(
            model_name='connection',
            name='name',
        ),
    ]
