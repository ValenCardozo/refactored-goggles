from django.urls import path

from home.views import home

urlpatterns = [
    path(
        route='home/',
        view=home,
        name='home'
    ),
]