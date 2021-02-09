import uuid
from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from users.models import User
from orchestra.models import Orchestra

class PracticeInfo(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    
    title = models.CharField(_('タイトル'), max_length=300)
    content = models.CharField(_('内容'), max_length=3000)
    orchestra = ForeignKey(Orchestra, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'PracticeInfo'
        verbose_name = _('practice_info')
        verbose_name_plural = _('練習に関するお知らせ')
    
    def get_full_name(self):
        return self.title
