# Generated by Django 4.1.7 on 2023-03-15 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DimComponentType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=13, unique=True)),
                ('value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MapComponent',
            fields=[
                ('component_id', models.AutoField(primary_key=True, serialize=False)),
                ('ext_device_id', models.IntegerField()),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.dimcomponenttype')),
            ],
            options={
                'unique_together': {('ext_device_id', 'type_id')},
            },
        ),
        migrations.CreateModel(
            name='FctRecord',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('value', models.FloatField()),
                ('component_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.mapcomponent')),
            ],
        ),
        migrations.CreateModel(
            name='AvgRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('value', models.FloatField()),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.dimcomponenttype')),
            ],
        ),
    ]
