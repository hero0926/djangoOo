"""hero URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings

# 내 프로젝트 안 어쩌구 /xxx/mypage.hero 에서 xxx 쪽을 연결 <- 이거용어가 기억이안남
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
]


# 디버그 툴바

if settings.DEBUG:
    import debug_toolbar

# 디버그 설정되어 있으면 디버그 모드 설정
urlpatterns += [
    url(r'^__debug__/', include(debug_toolbar.urls)),
]