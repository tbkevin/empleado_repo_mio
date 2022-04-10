from tokenize import blank_re
from django.db import models
from ckeditor.fields import RichTextField 
from applications.departamento.models import Departamento
# Create your models here.
class Habilidades(models.Model):
	habilidad = models.CharField('Habilidad', max_length=50)

	class Meta:
		verbose_name = 'Habilidad'
		verbose_name_plural = 'Habilidad Empleados'
		ordering = ['habilidad']
	def __str__(self):
		return str(self.id) + '-'+self.habilidad

class Empleado(models.Model):
	JOB_CHOICES = (
		('0','Contador'),
		('1','Administrador'),
		('2','Economista'),
		('3','OTRO'),
		)
	first_name = models.CharField('Nombres', max_length=60)
	last_name  = models.CharField('Apellidos', max_length=60)
	full_name  = models.CharField(
		'Nombre completo', 
		max_length=60,
		blank=True)
	job  = models.CharField('Trabajo', max_length=1,choices=JOB_CHOICES)
	departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to='empleado',blank=True, null=True)
	habilidades = models.ManyToManyField(Habilidades)
	#hoja_vida = RichTextField()

	class Meta:
		verbose_name = 'Empleado'
		verbose_name_plural = 'Recursos humanos'
		#ordering = ['-first_name','last_name']
		ordering = ['id']
		#Para evitar una combinacion de atributos duplicados
		unique_together = ('first_name', 'departamento')

	def __str__(self):
		return str(self.id) + '-'+self.first_name + '-' + self.last_name
