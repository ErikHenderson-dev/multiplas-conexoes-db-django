from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .firstapp import views as firstappview
from .lastapp import views as lastappview

route = routers.DefaultRouter()

route.register(r'firstapp', firstappview.Contatos, basename="Firstapp")
route.register(r'lastapp', lastappview.ContatosNome, basename="Lastapp")

urlpatterns = [
    path('', include(route.urls)),
    path('admin/', admin.site.urls),
]
