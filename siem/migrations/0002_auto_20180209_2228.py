# Generated by Django 2.0.1 on 2018-02-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='limitrule',
            name='dest_host_filter',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='limitrule',
            name='source_host_filter',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
