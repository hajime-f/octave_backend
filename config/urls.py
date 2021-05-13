from django.urls import path, include
from django.contrib import admin
from dj_rest_auth.registration.views import VerifyEmailView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='octave API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiv1/auth/', include('dj_rest_auth.urls')),
    path('apiv1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('apiv1/auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='octave API')),
]
