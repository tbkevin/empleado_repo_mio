from django.apps import AppConfig

#Desde la 3.2 hay que modificar el name de la siguiente variable
#Para ello, debemos poner la ruta de nuestra aplicacion
class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.departamento'
