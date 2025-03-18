# Django Application

## Descripción
Esta es una aplicación desarrollada en Django que proporciona un crud y una autenticación basica.

## Requisitos previos
Antes de comenzar, asegúrate de tener instalado lo siguiente:
- Python 3.x
- Django 5.x
- Virtualenv (opcional pero recomendado)
- PostgreSQL

## Instalación

### 1. Clonar el repositorio
```bash
    git clone https://github.com/kira2222/Aula.git
    cd Aula
```

### 2. Crear y activar un entorno virtual (opcional pero recomendado)
```bash
    python -m venv venv
    source venv/bin/activate  # En macOS y Linux
    venv\Scripts\activate     # En Windows
```

### 3. Instalar dependencias
```bash
    pip install -r requirements.txt
```

### 4. Configurar la base de datos
Modifica el archivo `settings.py` para configurar la base de datos.
Ejecuta las migraciones:
```bash
    python manage.py migrate
```

### 5. Crear un superusuario (opcional)
```bash
    python manage.py createsuperuser
```

### 6. Ejecutar el servidor
```bash
    python manage.py runserver
```
Accede a la aplicación en `http://127.0.0.1:8000/`.

## Estructura del proyecto
```
    AULA/
│── accounts/
│   │── migrations/
│   │── templates/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── urls.py
│   │── views.py
│
│── AulaMatriz/
│   │── __pycache__/
│   │── __init__.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── tasks/
│   │── migrations/
│   │── templates/
│   │── __init__.py
│   │── admin.py
│   │── apps.py
│   │── forms.py
│   │── models.py
│   │── tests.py
│   │── urls.py
│   │── views.py

```



## Contribución
Si deseas contribuir, crea un fork del repositorio, realiza tus cambios en una nueva rama y envía un pull request.

## Licencia
Este proyecto está bajo la licencia [nombre de la licencia].

