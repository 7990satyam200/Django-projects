from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.func.as_view(), name='home'),
]
