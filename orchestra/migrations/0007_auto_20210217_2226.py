# Generated by Django 3.1.4 on 2021-02-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestra', '0006_auto_20210216_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='orchestra',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='有効/無効'),
        ),
        migrations.AlterField(
            model_name='orchestra',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日時'),
        ),
        migrations.AlterField(
            model_name='orchestra',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]