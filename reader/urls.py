from django.conf.urls import url
from . import views

app_name = 'reader'

urlpatterns = [
    url(r'^$', views.parse),
    url(r'^parse$', views.parse, name='parse'),
    url(r'^diagram$', views.diagram, name='diagram'),
]
