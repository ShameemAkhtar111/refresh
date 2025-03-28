# Generated by Django 5.1.6 on 2025-03-18 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageprocess', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgroup',
            name='group_name',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_name', models.CharField(max_length=20)),
                ('process_env', models.CharField(max_length=10)),
                ('process_report', models.CharField(max_length=100)),
                ('process_state', models.CharField(default='stopped', max_length=10)),
                ('process_last_run', models.DateTimeField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageprocess.pgroup')),
            ],
        ),
    ]
