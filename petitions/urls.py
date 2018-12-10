"""petitions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
from django.urls import include, path
import django_cas_ng.views as cas_views

urlpatterns = [
    path('', include('index.urls')),
    path('admin/', admin.site.urls),
    url(r'', include('mama_cas.urls')),
    url(r'^accounts/login$', cas_views.LoginView, name='cas_ng_login'),
    url(r'^accounts/logout$', cas_views.LogoutView, name='cas_ng_logout'),
    url(r'^accounts/callback$', cas_views.CallbackView, name='cas_ng_proxy_callback'),
]
