from django.conf.urls import url
from . import views

app_name = 'reader'

urlpatterns = [
    url(r'^$', views.diagram),
    url(r'^index$', views.index, name='index'),
    url(r'^parse$', views.parse, name='parse'),
    url(r'^diagram$', views.diagram, name='diagram'),
]
