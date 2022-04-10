from django.shortcuts import render
from django.views.generic import (TemplateView, 
ListView, 
CreateView)
from .models import Prueba
from .forms import PruebaForm
class PruebaView(TemplateView):
#Con el template_name indicamos la direccion del archivo html
#En nuestro caso, django lo busca desde la carpeta indicada para templates
#en el archivo de configuracion base.py
#Por defecto, lo busca en una carpeta llamada templates de nuestra appliacation

	template_name = 'home/prueba.html'


class RFView(TemplateView):
	template_name = 'home/r_f.html'

class PruebaListView(ListView):
	template_name = "home/lista.html"
	context_object_name = 'listaNumeros'
	queryset = ['1','10','20','30']


class ListarPrueba(ListView):
	template_name = "home/lista_prueba.html"
	model = Prueba
	context_object_name = 'listaPrueba'
	

class PruebaCreateView(CreateView):
	template_name = "home/add.html"
	model = Prueba
	form_class = PruebaForm
	success_url = "/"
