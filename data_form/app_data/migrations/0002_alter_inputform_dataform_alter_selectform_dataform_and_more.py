# Generated by Django 4.0.5 on 2022-06-09 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputform',
            name='dataForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_forms', to='app_data.dataform'),
        ),
        migrations.AlterField(
            model_name='selectform',
            name='dataForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='select_forms', to='app_data.dataform'),
        ),
        migrations.AlterField(
            model_name='textareaform',
            name='dataForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='textarea_forms', to='app_data.dataform'),
        ),
    ]
