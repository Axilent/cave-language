"""cavelanguage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = patterns('cavelanguage.views',
    url(r'^$','home'),
    url(r'^symbols/$','symbol_library'),
    url(r'^symbol/(?P<slug>[\w-]+)/$','symbol'),
    url(r'^collection/(?P<slug>[\w-]+)/$','collection'),
    url(r'^collection/(?P<collection_slug>[\w-]+)/category/(?P<slug>[\w-]+)/$','category'),
    url(r'^diagram/(?P<diagram_id>\d+)/(?P<diagram_slug>[\w-]+)/$','diagram'),
    url(r'^diagrams/$','diagrams'),
    url(r'^contributors/$','contributors'),
)

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
