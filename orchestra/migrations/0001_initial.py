# Generated by Django 3.1.4 on 2021-01-10 06:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orchestra',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('orchestra_name', models.CharField(max_length=150, verbose_name='楽団名')),
                ('orchestra_name_kana', models.CharField(max_length=150, verbose_name='楽団名（かな）')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='メールアドレス')),
                ('orchestra_type', models.CharField(choices=[('吹奏楽団', '吹奏楽団'), ('交響楽団', '交響楽団'), ('合唱団', '合唱団'), ('ブラスバンド', 'ブラスバンド'), ('アンサンブル', 'アンサンブル'), ('その他', 'その他')], max_length=20, verbose_name='種別')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='設立年月日')),
                ('country', models.CharField(default='日本', editable=False, max_length=15, verbose_name='国')),
                ('postal_code', models.CharField(blank=True, max_length=7, null=True, verbose_name='郵便番号（ハイフンなし）')),
                ('prefecture', models.CharField(blank=True, max_length=5, null=True, verbose_name='都道府県')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='市区町村番地')),
                ('building', models.CharField(blank=True, max_length=30, null=True, verbose_name='建物名')),
                ('tel', models.CharField(blank=True, max_length=11, null=True, verbose_name='電話番号（ハイフンなし）')),
                ('url', models.URLField(blank=True, max_length=300, null=True, verbose_name='URL')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真')),
            ],
            options={
                'verbose_name': 'orchestra',
                'verbose_name_plural': '楽団',
                'db_table': 'Orchestra',
            },
        ),
    ]
