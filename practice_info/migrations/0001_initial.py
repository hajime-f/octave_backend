# Generated by Django 3.1.4 on 2021-06-28 07:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orchestra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeInfo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=300, verbose_name='タイトル')),
                ('content', models.CharField(max_length=3000, verbose_name='内容')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('is_active', models.BooleanField(default=True, verbose_name='有効/無効')),
                ('orchestra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orchestra.orchestra')),
            ],
            options={
                'verbose_name': 'practice_info',
                'verbose_name_plural': '練習に関するお知らせ',
                'db_table': 'PracticeInfo',
            },
        ),
    ]
