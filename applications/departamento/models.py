from django.db import models

# Create your models here.
class Departamento(models.Model):
	#mc para CharField
	#mb para BooleanField
	#El primer parametro es para indicar el texto que figurarA
	#en el ORM de Django
	name = models.CharField('Nombre',max_length=50)
	shor_name = models.CharField('Nombre corto',max_length=20,unique=True)
	anulate = models.BooleanField('Anulado',default=False)

	class Meta:
		verbose_name = 'Mi departamento'
		verbose_name_plural = 'Areas de la empresa'
		ordering = ['id']
		#Para evitar una combinacion de atributos duplicados
		unique_together = ('name','shor_name')
	
	def __str__(self):
		return str(self.id) + '-'+self.name + '-' + self.shor_name