# Generated by Django 5.0.2 on 2024-03-21 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0043_alter_rmetamessage_cdc_payload_json'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sourcesystem',
            name='is_intermediary',
        ),
        migrations.AddField(
            model_name='sourcesystem',
            name='program_area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report_metadata.programareatype'),
        ),
    ]