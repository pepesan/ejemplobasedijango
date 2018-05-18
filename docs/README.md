## Proyecto de Pruebas de Django 2
### Instalación
Para empezar necesitaremos disponer de un entorno de desarrollo con Python 3.6 en dicho entorno deberemos realizar la instalación de django2
### Proyecto Realizado
El proyecto se ha realizado desde 0 con el generador que integra django 2
>django-admin startproject mysite
###Se ha arrancado el servidor
> python manage.py runserver
### Se ha creado un módulo de polls
>python manage.py startapp polls
### Se ha actualizado el modelo una vez modificado el models.py
>python manage.py migrate
### Se crean los ficheros de migración
>python manage.py makemigrations polls
### Se imprime el fichero de migración
>python manage.py sqlmigrate polls 0001
### Se pueden hacer consultas a la bbdd 
>python manage.py shell
### se crea el superusuario
>python manage.py createsuperuser
### En la app del ejemplo
* Usuario: admin
* Contraseña: rootroot
* Ya se debería poder acceder a la [ruta de admin](http://localhost:8000/admin) 
   


