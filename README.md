# Sistema de Orientación Vocacional 🎓
## Descripción
Sistema de gestión académica desarrollado con Django que permite la administración de universidades, clases, calificaciones y usuarios con roles específicos (estudiantes y profesores).

## 🌟 Características Principales
- 👥 Gestión de usuarios con roles (estudiantes y profesores)
- 🔐 Sistema de autenticación personalizado
- 🆔 Validación de cédula ecuatoriana
- 🏛️ Gestión de universidades con ubicación geográfica
- 📊 Sistema de calificaciones
- 🔒 Control de acceso basado en roles
## 📋 Modelos del Sistema
### 👤 Usuarios
- Estudiantes y Profesores con información personalizada
- Validación de cédula ecuatoriana
- Campos personalizados por rol
### 📚 Académico
- Universidades
- Clases
- Calificaciones
- Gestión geográfica (Países y Ciudades)
## 🔧 Requisitos Previos
1. Python 3.x
2. Pipenv (para gestión de entorno virtual)
## ⚙️ Instalación
1. Clonar el repositorio:    git clone [url-del-repositorio]

2. Navegar al directorio del proyecto: cd ProyectoCore

3. Instalar Pipenv: pip install pipenv

4. Instalar dependencias: pipenv install
pipenv install -r dependencias.txt

5. Activar el entorno virtual: pipenv shell

6. Realizar las migraciones: python manage.py makemigrations
python manage.py migrate

7. Crear superusuario:python manage.py createsuperuser

8. Iniciar el servidor: python manage.py runserver

📁 Estructura del Proyecto
ProyectoCore/
├── OrientacionVocacional/
│   ├── Core/
│   │   ├── templates/
│   │   ├── views.py
│   │   └── urls.py
│   ├── Academico/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── admin.py
│   └── Usuarios/
│       ├── models.py
│       └── admin.py
└── manage.py

## 👥 Roles y Funcionalidades
### 👨‍🎓 Estudiantes
- Registro en el sistema
- Visualización de calificaciones
- Acceso a información universitaria
  
### 👨‍🏫 Profesores
- Gestión de clases
- Asignación de calificaciones
- Gestión de estudiantes

## 📝 Notas Importantes
- Asegúrate de ejecutar pipenv install -r dependencias.txt después de instalar pipenv
- Configura las variables de entorno necesarias
- Verifica los permisos de usuario después de crear el superusuario
