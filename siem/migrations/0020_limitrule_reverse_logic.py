# Generated by Django 2.0.4 on 2018-04-10 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0019_auto_20180409_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='limitrule',
            name='reverse_logic',
            field=models.BooleanField(default=False),
        ),
    ]
