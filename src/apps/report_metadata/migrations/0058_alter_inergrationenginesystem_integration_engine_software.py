# Generated by Django 5.0.2 on 2024-03-25 18:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0057_rename_software_inergrationenginesystem_integration_engine_software_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inergrationenginesystem',
            name='integration_engine_software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inergration_engine_software', to='report_metadata.inergrationenginesoftware'),
        ),
    ]
