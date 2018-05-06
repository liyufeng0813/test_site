"""tenMINsWEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from tenMINsapp.views import index,detail,detail_comment,index_login,index_register,detail_vote,mycollection,myinfo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index,name="index"),
    url(r'^index/(?P<cate>[A-Za-z]+)$', index, name="index"),
    url(r'^detail/(?P<page_num>\d+)$',detail,name="detail"),
    url(r'^detail/vote/(?P<page_num>\d+)$',detail_vote,name="vote"),
    url(r'^detail/(?P<page_num>\d+)/comment$',detail_comment,name="detail_comment"),
    url(r'^index_login/$', index_login, name="index_login"),
    url(r'^index_register/$', index_register, name="index_register"),
    url(r'^logout/$', logout,{'next_page': '/index'}, name="logout"),
    url(r'^mycollection/$', mycollection, name="mycollection"),
    url(r'^myinfo/$', myinfo, name="myinfo"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
