

from .views import ProfileDetailView 
from django.conf.urls import url

app_name = "profiles"

urlpatterns = [
    url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name="detail"),
   
]

