# 🎯 MyWhish_CRUD

Aplicación CRUD desarrollada con Django para gestionar una lista de deseos (Wishlist). Permite crear, leer, actualizar y eliminar elementos, incluyendo imágenes y descripciones. El proyecto está enfocado en la funcionalidad y se conecta a una base de datos MySQL usando phpMyAdmin.

---

## 🚀 Tecnologías utilizadas

-  Python 3.12
-  Django  
-  MySQL (administrado vía phpMyAdmin)  
-  Pillow (para la gestión de imágenes)  
-  Bootstrap (para los estilos visuales)

---

## ⚙️ Instalación y ejecución

Sigue estos pasos para clonar y correr el proyecto localmente:

# Clona el repositorio
git clone https://github.com/Z-FranXx/MyWhish_CRUD.git

# Entra a la carpeta del proyecto
cd MyWhish_CRUD

# Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
# Activa el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instala las dependencias
-  Django==5.2
-  mysqlclient==2.2.7
-  Pillow==11.1.0

# Crea la base de datos en MySQL usando phpMyAdmin (por ejemplo: mywhish_crud)

# Asegúrate de tener configurado el acceso a MySQL en settings.py:
 DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
         'NAME': 'mywhish_crud',
         'USER': 'root',
         'PASSWORD': '',
         'HOST': 'localhost',
         'PORT': '3306',
     }
 }

# Aplica las migraciones
python manage.py makemigrations
python manage.py migrate

# Ejecuta el servidor local
python manage.py runserver
