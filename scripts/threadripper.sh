#!/bin/bash

killall streamlit

# Script para iniciar Threadripper y seleccionar el archivo de logs
# Usa un script Python para abrir el diálogo de selección de archivos
LOG_FILE=$(
  python3 - <<END
import tkinter as tk
from tkinter import filedialog
import os

# Inicializar Tkinter y ocultar la ventana principal
root = tk.Tk()
root.withdraw()

# Abrir el selector de archivo
file_path = filedialog.askopenfilename(title="Selecciona el archivo de logs", filetypes=[("Archivos de log", "*.log"), ("Todos los archivos", "*.*")])

# Si se selecciona un archivo, imprime la ruta absoluta
if file_path:
    print(os.path.abspath(file_path))
END
)

# Verifica si el usuario seleccionó un archivo
if [ -z "$LOG_FILE" ]; then
  echo "No se seleccionó ningún archivo. Saliendo..."
  exit 1
fi

# Ejecuta Threadripper con la ruta absoluta del archivo de logs seleccionado
streamlit run /opt/threadripper/threadripper.py -- "$LOG_FILE"
