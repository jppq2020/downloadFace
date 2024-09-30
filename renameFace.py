import os

# Directorio de las imágenes existentes (las que ya tienen nombres)
existing_images_dir = "/Users/rigel/Dev/python/imagenes"

# Directorio de las imágenes recién descargadas
downloaded_images_dir = "/Users/rigel/Dev/python/nuevas"

# Obtener los nombres de las imágenes existentes
existing_images = sorted(os.listdir(existing_images_dir))

# Obtener las imágenes descargadas
downloaded_images = sorted(os.listdir(downloaded_images_dir))

if not os.path.exists(existing_images_dir):
    print(f"El directorio {existing_images_dir} no existe.")
else:
    # Verificar si la cantidad de imágenes es la misma
    if len(existing_images) != len(downloaded_images):
        print("La cantidad de imágenes descargadas no coincide con las existentes.")
    else:
        # Renombrar las imágenes descargadas con los nombres de las imágenes existentes
        for i in range(len(downloaded_images)):
            old_path = os.path.join(downloaded_images_dir, downloaded_images[i])
            new_name = existing_images[i]
            new_path = os.path.join(downloaded_images_dir, new_name)
            
            # Renombrar el archivo
            os.rename(old_path, new_path)
            print(f"Imagen {downloaded_images[i]} renombrada a {new_name}")

    print("Proceso de renombrado completado.")
