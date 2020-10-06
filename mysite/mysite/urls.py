"""mysite URL Configuration

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
from django.conf.urls import include
from django.contrib import admin
from django.views.generic.base import TemplateView
from mmm.views import GymListView, GymDetailView, GymCreateView, GymUpdateView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view
from menus.views import HomeView
from django.contrib.auth import views as auth_views
#from profiles.views import ActivateView
from django.contrib.auth.views import (LoginView,
 LogoutView,
PasswordChangeView,
PasswordChangeDoneView,
PasswordResetView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView
)

# from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^about/$', TemplateView.as_view(template_name='About.html'), name="about"),
    url(r'^contact/$', TemplateView.as_view(template_name='Contact.html'), name="contact"),
    url(r'^Gym/', include('mmm.urls', namespace='mmm')),
    #url(r'^activation/$', ActivateView.as_view(), name = 'active'),
    url(r'^profile/', include('profiles.urls', namespace="profiles")),
    url(r'^item/', include('menus.urls', namespace= "menus" )),
    # url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^register/$', RegisterView.as_view(), name = 'register'),
    url(r'^activate/(?P<code>[a-z0-9].*)/$', activate_user_view, name='activate'),
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^logout/$', LogoutView.as_view(), name = 'logout'),
    url(r'^profile-follow/$', ProfileFollowToggle.as_view(), name="follow"),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name="password_change_done"),

    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name="password_change"),

    url(r'^password_reset/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_reset_done.html'), name="password_reset_done"),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name="password_reset"),

    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name="password_reset_complete"),
    
    
]



