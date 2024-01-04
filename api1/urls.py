from django.contrib import admin
from django.urls import path,include
from . import views

from api1.views import MovieViewSet,collectionsViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'movies',MovieViewSet)

router.register(r'collection',collectionsViewSet)
urlpatterns = [
    
    path("",views.home,name="home"),
    path("api",include(router.urls))
]
