# Generated by Django 3.1.4 on 2021-01-10 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0002_orchestra_admin_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='orchestra',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]
