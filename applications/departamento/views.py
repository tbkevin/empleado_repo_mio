from django.shortcuts import render
from django.views.generic.edit import FormView

from applications import departamento
# Create your views here.
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento
from django.views.generic import (
	ListView,)

class DepartamentoListView(ListView):
	model = Departamento
	template_name = "departamento/lista.html"
	context_object_name = "departamentos"



class NewDepartamentoView(FormView):
	template_name = "departamento/new_departamento.html"
	form_class = NewDepartamentoForm
	success_url = "/"

	def form_valid(self, form):
		print("****estamos en el form valid****")
		depa = Departamento(
			name=form.cleaned_data['departamento'],
			shor_name=form.cleaned_data['shorname']
		)
		depa.save()

		nombre = form.cleaned_data['nombre']
		apellidos = form.cleaned_data['apellidos']
		Empleado.objects.create(
			first_name = nombre,
			last_name = apellidos,
			full_name = nombre + apellidos,
			job = '1',
			departamento=depa

		)
		return super(NewDepartamentoView, self).form_valid(form)
