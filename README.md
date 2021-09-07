# instalar el aplicativo  e instalar las librerias requeridas
git clone https://github.com/oal2727/django_cv

# 1.Prepara las migraciones
python manage.py makemigrations

# 2.Ejecutar las migraciones
python manage.py migrate

# 3.Crear usuario de acceso
python manage.py createsuperuser

# 4.Habilitar server
python manage.py runserver