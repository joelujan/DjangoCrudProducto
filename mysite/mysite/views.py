from django.shortcuts import render, redirect

from mysite.forms import ProductoForm
from mysite.models import Producto


def listar_productos(request):
    productos = Producto.objects.all() #SELECT * FROM producto
    return render(request, 'listar_productos.html', {'productos':productos})

def crear_producto(request):
    producto = Producto(nombre=request.POST['producto'], precio= request.POST['precio'], descripcion=request.POST['descripcion'],
                        fecha_creacion=request.POST['fecha_creacion'])
    producto.save()
    return redirect('productos')

def eliminar_producto(request, producto_id):
    eliminar_producto = Producto.objects.get(id = producto_id)
    eliminar_producto.delete()
    return redirect('productos')

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    forms = ProductoForm(request.POST or None, instance=producto)
    if forms.is_valid() and request.POST:
        forms.save()
        return redirect('productos')
    return render(request, 'editar_producto.html', {'forms': forms})