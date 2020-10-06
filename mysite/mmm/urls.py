from django.conf.urls import url
from mmm.views import (

	GymListView,
    GymDetailView,
    GymCreateView,
    GymUpdateView,
    

)

app_name = 'mmm'

urlpatterns = [
    url(r'^Gymlist/$', GymListView.as_view(), name="list"),
    url(r'^create/$', GymCreateView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', GymUpdateView.as_view(), name="detail"),
    
]
