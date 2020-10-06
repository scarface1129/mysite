from django.conf.urls import url
from mmm.views import (

	Gymlistview,
    GymDetailView,
    GymCreateView,
    Gym_listview

)

app_name = 'mmm'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', GymDetailView.as_view(), name="detail"),
    url(r'^create/$', GymCreateView.as_view(), name="create"),
    url(r'^$', Gym_listview.as_view(), name="gym")
    
]
