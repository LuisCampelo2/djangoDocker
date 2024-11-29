from django.contrib import admin
from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('',views.index, name='index'),
    path('cadastramento', views.cadastrar_user, name='cadastro'),
    path('admin/', admin.site.urls),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('update',views.update_view,name='update_view'),
    path('meuperfil',views.meu_perfil,name='meuPerfil'),
]