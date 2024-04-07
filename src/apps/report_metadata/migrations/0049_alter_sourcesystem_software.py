# Generated by Django 5.0.2 on 2024-03-21 20:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0048_alter_sourcesystem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sourcesystem',
            name='software',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='report_metadata.sourcesoftware'),
        ),
    ]