from django.shortcuts import  render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "aplicacion/index.html")


def aboutme(request):
    return render(request,"aplicacion/aboutme.html")

#Cargos----------------------------------------------------------------------------------------------
def listaCargos(request):
    cargos = Cargos.objects.all()
    ctx = {"lista_cargoss": cargos}

    return render(request, "aplicacion/listaBermudas.html", ctx)
def listaCargos(request):
    cargos = Cargos.objects.all()
    ctx = {"lista_cargos": cargos }
    return render(request, "aplicacion/listaCargos.html", ctx)

@login_required
def cargos(request): 
    cargos = Cargos.objects.all()
    ctx = {"cargos": cargos}
    return render(request, "aplicacion/cargos.html", ctx)

@login_required
def cargosForm(request):
    if request.method == "POST":                
        cargos = Cargos(nombre=request.POST['nombre'], color=request.POST['color'],
                        talle=request.POST['talle'], precio=request.POST['precio'])
        cargos.save()
    return render(request, "aplicacion/cargosForm.html")

@login_required
def eliminarCargo(request,id_cargo):
    cargo = Cargos.objects.get(id=id_cargo)
    cargo.delete()
    return redirect(reverse_lazy('cargos'))

@login_required
def updateCargo(request,id_cargo):
    cargo = Cargos.objects.get(id=id_cargo)
    if request.method == "POST":
        miForm = CargoForm(request.POST)
        if miForm.is_valid():
            cargo.nombre = miForm.cleaned_data.get('nombre')
            cargo.color = miForm.cleaned_data.get('color')
            cargo.talle = miForm.cleaned_data.get('talle')
            cargo.save()
            return redirect(reverse_lazy('cargos'))
    else:
        miForm = CargoForm(initial={'nombre': cargo.nombre,
                                   'color': cargo.color,
                                   'talle': cargo.talle })
    return render(request, "aplicacion/cargosForm.html", {'form':miForm})

#Bermudas------------------------------------------------------------------------------------------
def listaBermudas(request):
    bermudas = Bermudas.objects.all()
    ctx = {"lista_bermudas":  bermudas }
    return render(request, "aplicacion/listaBermudas.html", ctx)

@login_required
def bermudas(request):
    bermudas = Bermudas.objects.all()
    ctx =  {"bermudas": bermudas}
    return render(request, "aplicacion/bermudas.html", ctx)

@login_required
def bermudasForm(request):
    if request.method == "POST":                
        bermudas = Bermudas(nombre=request.POST['nombre'], color=request.POST['color'],
                        talle=request.POST['talle'], precio=request.POST['precio'])
        bermudas.save()
    return render(request, "aplicacion/bermudasForm.html")

@login_required
def eliminarBermuda(request,id_bermuda):
    bermuda = Bermudas.objects.get(id=id_bermuda)
    bermuda.delete()
    return redirect(reverse_lazy('bermudas'))

@login_required
def updateBermuda(request,id_bermuda):
    bermuda = Bermudas.objects.get(id=id_bermuda)
    if request.method == "POST":
        miForm = BermudaForm(request.POST)
        if miForm.is_valid():
            bermuda.nombre = miForm.cleaned_data.get('nombre')
            bermuda.color = miForm.cleaned_data.get('color')
            bermuda.talle = miForm.cleaned_data.get('talle')
            bermuda.save()
            return redirect(reverse_lazy('bermudas'))
    else:
        miForm = BermudaForm(initial={'nombre': bermuda.nombre,
                                   'color': bermuda.color,
                                   'talle': bermuda.talle })
    return render(request, "aplicacion/bermudasForm.html", {'form':miForm})


#Buzos------------------------------------------------------------------------------------------------
def listaBuzos(request):
    buzos = Buzos.objects.all()
    ctx = {"lista_buzos": buzos }
    return render(request, "aplicacion/listaBuzos.html", ctx)
    

def buscarBuzos(request):
    return render(request, "aplicacion/buscarBuzos.html")

def buscar(request):
    if request.GET['buzos']:
        buzos = request.GET['buzos']
        nombre = Buzos.objects.filter(nombre__icontains=buzos)
        return render(request, 
                      "aplicacion/resultadoBuzos.html", 
                      {"buzos": nombre})
    return HttpResponse("No se ingresaron datos para buscar!")


def buzos(request):
    buzos = Buzos.objects.all()
    ctx = {"buzos": buzos }
    return render(request, "aplicacion/buzos.html", ctx)

@login_required
def buzosForm(request):
    if request.method == "POST":                
        buzos = Buzos(nombre=request.POST['nombre'], color=request.POST['color'],
                    talle=request.POST['talle'], precio=request.POST['precio'])
        buzos.save()
    return render(request, "aplicacion/buzosForm.html")

@login_required
def eliminarBuzo(request,id_buzo):
    buzo = Buzos.objects.get(id=id_buzo)
    buzo.delete()
    return redirect(reverse_lazy('buzos'))

@login_required
def updateBuzo(request,id_buzo):
    buzo = Buzos.objects.get(id=id_buzo)
    if request.method == "POST":
        miForm = BuzoForm(request.POST)
        if miForm.is_valid():
            buzo.nombre = miForm.cleaned_data.get('nombre')
            buzo.color = miForm.cleaned_data.get('color')
            buzo.talle = miForm.cleaned_data.get('talle')
            buzo.save()
            return redirect(reverse_lazy('buzos'))
    else:
        miForm = BuzoForm(initial={'nombre': buzo.nombre,
                                   'color': buzo.color,
                                   'talle': buzo.talle })
    return render(request, "aplicacion/buzosForm.html", {'form':miForm})

#Remeras---------------------------------------------------------------------------------------------
def listaRemeras(request):
    remeras = Remeras.objects.all()
    ctx = {"lista_remeras": remeras }
    return render(request, "aplicacion/listaRemeras.html", ctx)

@login_required
def remeras(request):
    remeras =  Remeras.objects.all()
    ctx = {"remeras":remeras}
    return render(request, "aplicacion/remeras.html", ctx)

@login_required
def remerasForm(request):
    if request.method == "POST":                
       remeras = Remeras(nombre=request.POST['nombre'], color=request.POST['color'],
                      talle=request.POST['talle'], precio=request.POST['precio'])
       remeras.save()
    return render(request, "aplicacion/remerasForm.html")

@login_required
def eliminarRemera(request,id_remera):
    remera = Remeras.objects.get(id=id_remera)
    remera.delete()
    return redirect(reverse_lazy('remeras'))

@login_required
def updateRemera(request,id_remera):
    remera = Remeras.objects.get(id=id_remera)
    if request.method == "POST":
        miForm = RemeraForm(request.POST)
        if miForm.is_valid():
            remera.nombre = miForm.cleaned_data.get('nombre')
            remera.color = miForm.cleaned_data.get('color')
            remera.talle = miForm.cleaned_data.get('talle')
            remera.save()
            return redirect(reverse_lazy('remeras'))
    else:
        miForm = RemeraForm(initial={'nombre': remera.nombre,
                                   'color': remera.color,
                                   'talle': remera.talle })
    return render(request, "aplicacion/remerasForm.html", {'form':miForm})



#----------------------------------------------------------------------------------------------------

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render(request, "aplicacion/index.html", {"mensaje": f"Bienvenido/a {usuario}"})
            else:    
                return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Clave o Usuario incorrectos"})
        else:    
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": "Clave o Usuario incorrectos"})

    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form":miForm})


def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)  
        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/index.html", {"mensaje":"Su Usuario se ha creado con exito!"})        
    else:
        form = RegistroUsuariosForm() 

    return render(request, "aplicacion/registroUsuarios.html", {"form": form})   


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/index.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username}) 


@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0: 
                avatarViejo[0].delete()
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/index.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})
 
    
