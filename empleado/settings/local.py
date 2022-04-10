from .base import *
# .base el punto sirve para indicar que el archivo esta en la misma carpeta del scrip actual
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []





# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#Usamos el local para configurar la bbdd de postgres para que si
#en produccion quisiesemos trabajar con otra bbdd no haya problemas
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbempleado',
        'USER': 'kevin',
        'PASSWORD': 'KEVIN',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR/'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
