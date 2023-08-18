from django.urls import path, include
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),
    path('aboutme/', aboutme ,name="aboutme"),
#Remeras---------------------------------------------------------------------------------------------
    path('Lista_Remeras/', listaRemeras ,name="lista_remeras"),
    path('remeras/', remeras, name="remeras"),
    path('create_remeras/', remerasForm, name="create_remeras"),
    path('eliminar_remera/<id_remera>/', eliminarRemera, name="eliminar_remera"),
    path('update_remera/<id_remera>/', updateRemera, name="update_remera"),
#Cargos----------------------------------------------------------------------------------------------
    path('Lista_Cargos/', listaCargos, name="lista_cargos"),
    path('cargos/', cargos, name="cargos"),
    path('create_cargos/', cargosForm, name="create_cargos"),
    path('eliminar_cargo/<id_cargo>/', eliminarCargo, name="eliminar_cargo"),
    path('update_cargo/<id_cargo>/', updateCargo, name="update_cargo"),
#Bermudas--------------------------------------------------------------------------------------------
    path('Lista_Bermudas/', listaBermudas, name="lista_bermudas"),
    path('bermudas/', bermudas, name="bermudas"),
    path('create_bermudas/', bermudasForm, name="create_bermudas"),
    path('eliminar_bermuda/<id_bermuda>/', eliminarBermuda, name="eliminar_bermuda"),
    path('update_bermuda/<id_bermuda>/', updateBermuda, name="update_bermuda"),
#Buzos------------------------------------------------------------------------------------------------
    path('Lista_Buzos/', listaBuzos, name="lista_buzos"),
    path('buscar_buzos/', buscarBuzos, name="buscarbuzos"),
    path('buscar/', buscar, name="buscar"),
    path('create_buzos/', buzosForm, name="create_buzos"),
    path('buzos/', buzos, name="buzos"),
    path('eliminar_buzo/<id_buzo>/', eliminarBuzo, name="eliminar_buzo"),
    path('update_buzo/<id_buzo>/', updateBuzo, name="update_buzo"),
#------------------------------------------------------------------------------------------------------    
    path('login/', login_request, name="login"),   
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('RegistroUsuarios/', register, name="registro"),

    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    ]