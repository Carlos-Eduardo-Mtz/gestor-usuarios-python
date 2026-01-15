# Gestor de Usuarios en Python

Aplicación de consola desarrollada en Python para administrar usuarios utilizando Programación Orientada a Objetos.

## Descripción

Este programa permite gestionar usuarios normales y administradores desde una interfaz por consola.  
Incluye validación de correos electrónicos, almacenamiento de datos en archivos y opciones básicas de administración.

El sistema guarda la información en un archivo de texto para que los datos se conserven aunque se cierre el programa.

## Funcionalidades

- Agregar usuarios normales  
- Agregar usuarios administradores con nivel (root / admin)  
- Validación de correos electrónicos  
- Mostrar usuarios registrados  
- Eliminar usuarios  
- Guardar usuarios en archivo  
- Cargar usuarios desde archivo al iniciar  
- Manejo de errores por entradas inválidas  

## Tecnologías utilizadas

- Python 3  
- Programación Orientada a Objetos  
- Manejo de archivos de texto  

## Cómo usar el programa

1. Ejecutar el archivo principal:

python gestor_usuarios.py

2. Usar el menú interactivo para:

- Agregar usuarios  
- Mostrar usuarios  
- Eliminar usuarios  
- Salir del programa  

3. Al salir, los usuarios se guardarán automáticamente en el archivo usuarios.txt.

## Estructura del proyecto

gestor-usuarios-python/
│
├── gestor_usuarios.py
├── usuarios.txt
└── README.md

## Objetivo del proyecto

Este proyecto fue creado como práctica para reforzar conocimientos sobre:

- Clases y herencia  
- Métodos y atributos  
- Validación de datos  
- Manejo de listas  
- Persistencia con archivos  
- Uso de funciones como enumerate, split, strip e isinstance  

## Estado del proyecto

Proyecto funcional de práctica académica.

Posibles mejoras futuras:

- Edición de usuarios  
- Búsqueda de usuarios  
- Interfaz gráfica  
- Uso de base de datos  
