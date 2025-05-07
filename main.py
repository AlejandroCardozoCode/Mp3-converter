from pydub import AudioSegment
import os
import shutil

def convert_audio_to_mp3(source_folder, destination_folder):
    # Crea la carpeta de destino si no existe
    os.makedirs(destination_folder, exist_ok=True)

    # Extensiones soportadas
    supported_formats = ['.wav', '.ogg', '.flac', '.m4a', '.opus']

    # Itera sobre todos los archivos en la carpeta de origen
    for filename in os.listdir(source_folder):
        # Define la ruta completa del archivo de entrada y de salida
        file_path = os.path.join(source_folder, filename)
        file_name, file_extension = os.path.splitext(filename)
        
        # Verifica si el archivo es un .mp3
        if file_extension.lower() == '.mp3':
            # Copia el archivo .mp3 sin conversión
            shutil.copy(file_path, os.path.join(destination_folder, filename))
            print(f"{filename} it's already a mp3 file, copying...")
            continue
        
        # Verifica si el archivo es de un formato soportado para conversión
        if file_extension.lower() not in supported_formats:
            continue
        
        try:
            # Carga el archivo de audio y lo convierte a .mp3
            audio = AudioSegment.from_file(file_path)
            output_path = os.path.join(destination_folder, f"{file_name}.mp3")
            audio.export(output_path, format="mp3")
            print(f"Converting : {filename} -> {file_name}.mp3")
        
        except Exception as e:
            print(f"Error al convertir {filename}: {e}")

# Configuración de carpetas de origen y destino
source_folder = input("Source folder: ") 
destination_folder = input("Destination folder: ") 

# Ejecuta la conversión
convert_audio_to_mp3(source_folder, destination_folder)
