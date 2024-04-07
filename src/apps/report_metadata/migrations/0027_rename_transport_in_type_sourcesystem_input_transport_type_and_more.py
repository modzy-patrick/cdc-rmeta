# Generated by Django 5.0.2 on 2024-03-13 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0026_rename_other_supported_data_input_types_sourcesystem_input_data_other_types_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sourcesystem',
            old_name='transport_in_type',
            new_name='input_transport_type',
        ),
        migrations.RenameField(
            model_name='sourcesystem',
            old_name='transport_out_type',
            new_name='output_transport_type',
        ),
        migrations.AddField(
            model_name='sourcesystem',
            name='input_transport_other_types',
            field=models.ManyToManyField(blank=True, related_name='source_inport_transport_other_types', to='report_metadata.datatransporttype'),
        ),
        migrations.AddField(
            model_name='sourcesystem',
            name='output_transport_other_types',
            field=models.ManyToManyField(blank=True, related_name='source_output_data_other_types', to='report_metadata.datatransporttype'),
        ),
        migrations.AlterField(
            model_name='sourcesystem',
            name='input_data_other_types',
            field=models.ManyToManyField(blank=True, related_name='source_input_data_other_types', to='report_metadata.healthdatatype'),
        ),
        migrations.AlterField(
            model_name='sourcesystem',
            name='output_data_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='soure_data_output_type', to='report_metadata.healthdatatype'),
        ),
    ]
