"""redesolidariedade_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api_controll import viewsets

route = routers.DefaultRouter()

route.register(r'entidades', viewsets.EntidadeViewSet, basename='entidades')
route.register(r'usuario', viewsets.UsuarioViewSet, basename='usuario')
route.register(r'movimentos', viewsets.MovimentosViewSet, basename='movimentos')
route.register(r'familia', viewsets.FamiliaViewSet, basename='familia')
route.register(r'integrantes_familia', viewsets.IntegranteFamiliarViewSet, basename='integrantes_familia')
route.register(r'movimento_itens', viewsets.MovimentoItensViewSet, basename='movimentos_itens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
