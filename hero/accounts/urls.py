from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login', kwargs={
        'form_class' : LoginForm
    }),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={

        'next_page' : settings.LOGIN_URL,

    }),
]