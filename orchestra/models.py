import uuid
from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from users.models import User

class Orchestra(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    members = models.ManyToManyField(User, blank=True, related_name="members")
    admin_users = models.ManyToManyField(User, related_name="managers")
    
    orchestra_name = models.CharField(_('楽団名'), max_length=150)
    orchestra_name_kana = models.CharField(_('楽団名（かな）'), max_length=150)
    email = models.EmailField(_('代表メールアドレス'), unique=True)

    orchestra_type = models.CharField(_('種別'), max_length=20,
                                      choices=(('吹奏楽団','吹奏楽団'),
                                               ('交響楽団','交響楽団'),
                                               ('合唱団','合唱団'),
                                               ('ブラスバンド','ブラスバンド'),
                                               ('アンサンブル','アンサンブル'),
                                               ('その他','その他')))
    birthday = models.DateField(_('設立年月日'), blank=True, null=True)
    
    country = models.CharField(_('国'), default='日本', max_length=15, editable=False)
    postal_code = models.CharField(_('郵便番号（ハイフンなし）'), max_length=7, blank=True, null=True)
    prefecture = models.CharField(_('都道府県'), max_length=5, blank=True, null=True)
    address = models.CharField(_('市区町村番地'), max_length=50, blank=True, null=True)
    building = models.CharField(_('建物名'), max_length=30, blank=True, null=True)
    tel = models.CharField(_('電話番号（ハイフンなし）'), max_length=11, blank=True, null=True)
    
    url = models.URLField(_('URL'), max_length=300, blank=True, null=True)
    photo = models.ImageField(_('写真'), blank=True, null=True)

    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True, editable=False)
    is_active = models.BooleanField(_('有効/無効'), default=True)

    class Meta:
        db_table = 'Orchestra'
        verbose_name = _('orchestra')
        verbose_name_plural = _('楽団')
    
    def get_full_name(self):
        return self.orchestra_name

    def get_full_name_kana(self):
        return self.orchestra_name_kana
