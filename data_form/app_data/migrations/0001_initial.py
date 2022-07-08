# Generated by Django 4.0.5 on 2022-06-09 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Данные',
            },
        ),
        migrations.CreateModel(
            name='TextareaForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('data', models.TextField(verbose_name='textarea')),
                ('dataForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_data.dataform')),
            ],
        ),
        migrations.CreateModel(
            name='SelectForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('choices', models.JSONField(blank=True, null=True)),
                ('dataForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_data.dataform')),
            ],
        ),
        migrations.CreateModel(
            name='InputForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('data', models.CharField(max_length=200, verbose_name='input')),
                ('dataForm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_data.dataform')),
            ],
        ),
    ]
