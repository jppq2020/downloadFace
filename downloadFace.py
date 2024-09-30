import os
import requests

# Número de imágenes a descargar
num_images = 5

# Crear una carpeta para guardar las imágenes
if not os.path.exists('rostros'):
    os.makedirs('rostros')

# URL de la página que genera los rostros
url = 'https://thispersondoesnotexist.com'

# Descargar imágenes
for i in range(1, num_images + 1):
    try:
        # Descargar la imagen
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Guardar la imagen en la carpeta
            with open(f'rostros/rostro_{i}.jpg', 'wb') as f:
                f.write(response.content)
            print(f"Imagen {i} descargada con éxito")
        else:
            print(f"Error al descargar la imagen {i}")
    except Exception as e:
        print(f"Error en la descarga de la imagen {i}: {e}")

print("Descarga completa.")
