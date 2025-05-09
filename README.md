# AvastWare

AvastWare es un proyecto de ransomware simulado desarrollado en Python. El objetivo del proyecto es encriptar los archivos dentro de un directorio utilizando la biblioteca `cryptography`, mientras que al usuario se le presenta por medio de phising, un señuelo que simula ser un anti-virus comercial.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Dependencias](#dependencias)
- [Funcionalidades](#funcionalidades)
- [Advertencias](#advertencias)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Descripción



El ransomware encripta todos los archivos dentro de un directorio seleccionado por el usuario y genera un archivo de texto al final del proceso informando que los archivos han sido encriptados.

> **Nota importante**: Este proyecto es solo con fines educativos. No debe ser utilizado para actividades maliciosas.

## Instalación

Sigue los siguientes pasos para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

- **Python 3.8 o superior** instalado en tu máquina.
- **VS CODE** (o IDE de tu preferencia).

### Clonar el Repositorio

```bash
git clone https://github.com/tu_usuario/avastware.git
cd avastware
```
### Crear un Entorno Virtual
```bash
python -m venv venv
```

### Activar el Entorno Virtual
- En Windows:
```bash
venv\Scripts\activate
```
- En macOS/Linux:
```bash
source venv/bin/activate
```
### Instalar Dependencias
Dentro del entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```
### Uso
1. Coloca AvastWare actúa como una aplicación maliciosa que encripta archivos en segundo plano mientras engaña al usuario al presentarse como un anti-virus legítimo. 
2. Ejecuta el proyecto desde el archivo gui.py:
```bash
python decoy/gui.py
```
3. La aplicación presentará una interfaz de consola simulando un anti-virus comercial, mientras en segundo plano los archivos en el directorio serán encriptados.

4. Al finalizar el proceso, verás un mensaje informándote que los archivos han sido encriptados.

### Desencriptar archivos
Para desencriptar los archivos, necesitarías la clave privada generada durante el proceso de encriptación, que se envia al correo especificado en el archivo 'gui.py'.

## Estructura del Proyecto
```bash
AvastWare/         # Carpeta raíz del proyecto
│
├── venv/             # Entorno virtual (creado automáticamente)
│
├── src/              # Carpeta principal del código fuente
│   ├── __init__.py   # Archivo para inicialización del módulo
│   ├── encryptor.py  # Contiene las funciones para cifrado
│   ├── utils.py      # Utilidades generales como manejo de archivos
│
├── data/             # Carpeta para los archivos a encriptar
│   └── ...           # Archivos de ejemplo
│
├── templates/        # Carpeta para la pagina web
│   └── index.html    # Página Principal de la web
│
├── decoy/            # Carpeta con la interfaz señuelo de la app
│   └── gui.py
│
├── main.py           # Archivo principal que ejecuta el proyecto
│
├── requirements.txt  # Archivo de dependencias
│
└── README.md         # Documentación del proyecto
```
## Dependencias
- cryptography: Biblioteca utilizada para el cifrado de archivos.
- otras dependencias pueden agregarse en el futuro para funcionalidades adicionales.
### Instalación de Dependencias
Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```
## Funcionalidades
- Cifrado de directorios: Utiliza AES para encriptar archivos dentro de un directorio.
- Señuelo de anti-virus legítimo: Presenta una interfaz de consola que simula la de un anti-virus comercial mientras se ejecuta el cifrado en segundo plano.
- Generación de nota de rescate: Informa al usuario que sus archivos han sido encriptados.

## Advertencias
Este proyecto está diseñado con fines educativos únicamente. No debe ser utilizado para propósitos maliciosos ni para crear software malicioso. El uso indebido de este proyecto puede llevar a consecuencias legales.

## Contribución
Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama nueva (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz un commit (git commit -m 'Agrega nueva funcionalidad').
4. Haz un push a tu rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia
Este proyecto está bajo la licencia MIT - mira el archivo **LICENSE** para más detalles.