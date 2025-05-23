import os

from src.encryptor import encrypt_file, decrypt_file
from pathlib import Path
from dotenv import load_dotenv

# Directorio base
base_dir = Path(__file__).resolve().parent

# Ruta absoluta para una clave AES
key_path = base_dir / 'key' / 'aes_key.key'

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Ahora puedes acceder a las variables de entorno
email_user = os.getenv('EMAIL_USER')
email_pass = os.getenv('EMAIL_PASS')

def main():
    choice = input("¿Deseas cifrar (C) o descifrar (D) un archivo?: ").lower()

    if choice == 'c':
        file_path = Path(input("Introduce la ruta del archivo a cifrar: "))
        if file_path.is_file():
            encrypt_file(file_path)
        else:
            print("Archivo no encontrado.")
    elif choice == 'd':
        file_path = Path(input("Introduce la ruta del archivo a descifrar: "))
        if file_path.is_file():
            decrypt_file(file_path)
        else:
            print("Archivo no encontrado.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
