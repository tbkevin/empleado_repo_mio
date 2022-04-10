from dataclasses import fields
from multiprocessing import context
from pyexpat import model
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	TemplateView,
	UpdateView,
	DeleteView)
from .models import Empleado
from django.urls import reverse_lazy
from .forms import EmpleadoForm
class InicioView(TemplateView):
	template_name = "inicio.html"



class ListAllEmpleados(ListView):
	template_name = 'persona/list_all.html'
	#Con este atributo, se crea un objeto de paginacion automaticamente
	
	paginate_by = 4
	ordering = 'id'
	context_object_name = "empleados"
	def get_queryset(self):
		print("**************")
		palabra_clave = self.request.GET.get("kword",'')
		lista = Empleado.objects.filter(
                    full_name__icontains=palabra_clave)
		return lista


class ListaEmpleadosAdmin(ListView):
	template_name = 'persona/admin_empleados.html'
	#Con este atributo, se crea un objeto de paginacion automaticamente
	paginate_by = 10
	ordering = 'first_name'
	context_object_name = "empleados"
	model = Empleado


class ListByAreaEmpleado(ListView):
	template_name = 'persona/list_by_area.html'
	context_object_name = 'empleados'
	#Recogemos el valor de la url 
	def get_queryset(self):
		area = self.kwargs['shorname']
		lista = Empleado.objects.filter(
            departamento__shor_name=area)
		return lista


class ListEmpleadosByKword(ListView):
	template_name = 'persona/by_kword.html'
	context_object_name = 'empleados'

	def get_queryset(self):
		palabra_clave = self.request.GET.get("kword")
		lista = Empleado.objects.filter(
                    first_name=palabra_clave)
		return lista


class ListHabilidadesEmpleado(ListView):
	template_name = 'persona/habilidades.html'
	context_object_name = 'habilidades'
	def get_queryset(self):
		empleado = Empleado.objects.get(id=2)
		return empleado.habilidades.all()


class ListByTrabajoEmpleado(ListView):
	template_name = 'persona/list_by_trabajo.html'

	#Recogemos el valor de la url 
	def get_queryset(self):
		trabajo = self.kwargs['job']
		lista = Empleado.objects.filter(
            job=trabajo)
		return lista


class EmpleadoDetailView(DetailView):
	model = Empleado
	template_name = "persona/detail_empleado.html"
	#Para enviar una variable ajena a los atributos 
	# de la tabla a la que pertenece el objeto
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['titulo'] = 'Empleado del mes'
		return context


class SuccessView(TemplateView):
	template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
	model = Empleado
	template_name = "persona/add.html"
	#fields = ['first_name', 'last_name', 'job',
	# 'departamento','habilidades','avatar']
	form_class = EmpleadoForm
	success_url = reverse_lazy('persona_app:empleados_admin')

	def form_valid(self,form):
		empleado = form.save()
		empleado.full_name = empleado.first_name +' '+empleado.last_name
		empleado.save()
		return super(EmpleadoCreateView,self).form_valid(form)
 


class EmpleadoUpdateView(UpdateView):
	model = Empleado
	template_name = "persona/update.html"
	fields = ['first_name', 'last_name', 'job',
           'departamento', 'habilidades']
	success_url = reverse_lazy('persona_app:empleados_admin')


	#Post se ejecuta abtes que form_valid
	#El objeto POST contiene en forma de diccionario los valores
	#que envia el cliente
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		print(request.POST)
		print(request.POST['last_name'])
		return super().post(request, *args, **kwargs)

	def form_valid(self, form):

		return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
	model = Empleado
	template_name = "persona/delete.html"
	success_url = reverse_lazy('persona_app:empleados_admin')

 
