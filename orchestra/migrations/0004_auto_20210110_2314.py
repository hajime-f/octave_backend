# Generated by Django 3.1.4 on 2021-01-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0003_orchestra_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orchestra',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='代表メールアドレス'),
        ),
    ]