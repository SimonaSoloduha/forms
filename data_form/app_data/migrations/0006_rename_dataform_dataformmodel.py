# Generated by Django 4.0.5 on 2022-07-06 07:28

from django.db import migrations


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ('app_data', '0005_rename_dataform_inputform_data_form_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataForm',
            new_name='DataFormModel',
        ),
    ]
