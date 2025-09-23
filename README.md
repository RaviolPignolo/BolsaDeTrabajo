# BolsaDeTrabajo
### Proyecto para la materia Programación Web 2 de la Universidad de Chubut

![UDC](https://img.shields.io/badge/Académico-Universidad%20del%20Chubut-5A7C92?logo=university&logoColor=white)

![Website](https://img.shields.io/badge/ProjectType:Web-App-informational)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.2.6-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite)
![Last Commit](https://img.shields.io/github/last-commit/RaviolPignolo/BolsaDeTrabajo)



Link del Figma de la página: [Bolsa de Trabajo Figma](https://www.figma.com/design/ZRwGIdXQ5dnz2rKJF8VbeJ/Web2-Proyecto?node-id=14-10&t=BcIimlqSLXCdP9Yh-1)

## Cómo levantar el entorno de trabajo

### 1. Crear y/o activar el entorno virtual
- Desde la raíz del proyecto activar el entorno virtual con
```bash
    source venv/bin/activate
```
- De no tener un entorno virtual crear uno usando
```bash
    python -m venv venv    
```
-  Activar el entorno virtual e instalar las dependencias
```bash
    pip install -r requirements.txt
```
### 2. Activar el entorno de Django
- Mediante los comandos cd / cd.. moverse hasta la carpeta "bolsa_de_trabajo" que contiene el archivo manage.py

- Hacer migración del manage.py para actualizar la base de datos en tu dispositivo
```bash
    python manage.py migrate
```

- Iniciar el servidor local para poder acceder a la página
```bash
    python manage.py runserver
```

- Acceder al link desde el navegador. Normalmente el link otorgado es: http://127.0.0.1:8000/

- De encontrar un error 404 agregar la siguiente dirección: /core/home. http://127.0.0.1:8000/core/home

## Participantes
- Leandro Pérez Pignolo
- Leonardo Daniel Nina
- Gabriel Campos Kray
- Santiago Gabriel Cañumir Palleres
