from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Wishlist
from .forms import ListForm
from django.http import Http404
from django.contrib import messages

# Create your views here.

# Acceder a la pagina de inicio
def inicio(request):
    return render(request, 'pages/inicio.html')

# Acceder a la whislist
def wishlist_view(request):
    lists = Wishlist.objects.all() # Obtener todos los elementos de la lista
    return render(request, 'whislist/frame.html', {'lists': lists})

# Vista para crear nuevos elementos en la wishlist
def create(request):
    form = ListForm(request.POST or None, request.FILES or None) # Crear el formulario
    if form.is_valid():
        form.save() # Guardar el formulario
        messages.success(request, "Elemento agregado correctamente a la Wishlist.")
        return redirect('whislist') # Redirigir a la whislist
    return render(request, 'whislist/create.html', {'form': form}) # Enviar el formulario a la vista

# Acceder a editar
def edit(request, id):
    item = Wishlist.objects.get(id=id) # Obtener el elemento a eliminar a traves del id
    form = ListForm(request.POST or None, request.FILES or None, instance=item) # Crear el formulario
    if form.is_valid() and request.POST:
        form.save() # Guardar el formulario
        return redirect('whislist')
    return render(request, 'whislist/edit.html', {'form': form}) # Enviar el formulario a la vista

# Eliminar elemento
def delete(request, id):
    try:
        item = Wishlist.objects.get(id=id)
        print(f"Eliminando item con id: {id}")  # Verifica que el item sea el correcto
        item.delete()
        print("Elemento eliminado")
    except Wishlist.DoesNotExist:
        print("Elemento no encontrado")
        raise Http404("El elemento no existe")
    
    return redirect('whislist')
