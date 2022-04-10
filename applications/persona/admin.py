from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = (
		'first_name',
		'last_name',
		'departamento',
		'job',
		#Es una columna especial en el despliegue de empleados
		#que no es atribuyto de la tabla Empleado. Puede ser util
		'full_name',
		'id'
	)

	def full_name(self,obj):
		print(obj)
		return obj.first_name +' '+ obj.last_name

	#Como es una tupla, siempre se coloca una coma
	search_fields = ('first_name',)
	list_filter = ('job','habilidades','departamento')
	#Este atributo es para colocar un cuadro de busqueda para habilidades
	#cuando creemos un nuevo empleado.
	filter_horizontal = ('habilidades',)



admin.site.register(Empleado, EmpleadoAdmin)

