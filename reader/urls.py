from django.conf.urls import url
from . import views

app_name = 'reader'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^diagram$', views.diagram, name='diagram'),
]
