"""mentoring_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from ment_form.views import fp, fp1, fp2, user_logout,fp3,send_mail,otp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', fp),
    url(r'^landlord/$', fp1, name="fp1"),
    url(r'^tenant/$', fp2, name="fp2"),
    url(r'^logout/$', user_logout),
    url(r'^search/$', fp3, name="fp3"),
    url(r'^send_mail/', send_mail, name="send_mail"),
    url(r'^otp/', otp, name="otp"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

