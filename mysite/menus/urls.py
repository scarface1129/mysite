from django.conf.urls import url
from .views import ItemCreateView, ItemDetailView, ItemListView, ItemUpdateView



app_name = "menus"


urlpatterns = [
    url(r'^$', ItemListView.as_view(), name="list"),
    url(r'^create/$', ItemCreateView.as_view(), name="create_item"),
    #url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name="update"),    
    url(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name="detail"),


]
