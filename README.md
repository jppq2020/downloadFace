# Proyecto de Descarga de Rostros

Este proyecto permite descargar rostros aleatorios generados desde la página web [This Person Does Not Exist](https://thispersondoesnotexist.com/). Utilizando un script en Python, se descargan automáticamente las imágenes a una carpeta local.

## Requerimientos

- **Python 3.6+**: Asegúrate de tener una versión de Python compatible instalada en tu sistema.

## Instalación

Sigue los pasos a continuación para configurar y ejecutar el proyecto:

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

git clone https://github.com/jppq2020/downloadFace.git
cd downloadFace

### Es recomendable crear un entorno virtual para aislar las dependencias del proyecto. Puedes hacerlo con los siguientes comandos:

python3 -m venv myenv

### En macOS y Linux:
source myenv/bin/activate

### En Windows:
myenv\Scripts\activate

### Instala las dependencias del proyecto especificadas en el archivo requirements.txt:

pip install -r requirements.txt

### Para iniciar la descarga de rostros, simplemente ejecuta el script downloadFace.py:

python downloadFace.py

### Una vez que termines de usar el entorno, puedes desactivarlo con el siguiente comando:

deactivate

downloadFace.py: Script principal para descargar las imágenes.
requirements.txt: Archivo que contiene las dependencias necesarias para el proyecto.
rostros/: Carpeta donde se guardarán las imágenes descargadas.

