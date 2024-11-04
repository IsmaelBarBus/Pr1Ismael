import subprocess
import win32clipboard
import time
import os

def descargar_y_monitorizar(ftp_url, nombre_archivo):
    # Abrir el proceso FTP y enviar comandos
    proceso = subprocess.Popen(
        ["ftp", ftp_url], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Enviar comandos FTP con correo electrónico como contraseña
    proceso.stdin.write("USER anonymous\n")
    proceso.stdin.write("PASS anonymous\n")  # Usa un correo ficticio
    proceso.stdin.write("dir\n")  # Listar archivos para confirmar conexión y existencia del archivo
    proceso.stdin.write(f"get {nombre_archivo}\n")
    proceso.stdin.write("quit\n")
    
    salida, error = proceso.communicate()

    # Mostrar salida de la lista de archivos para diagnosticar el problema
    print("Salida del comando FTP:\n", salida)

    # Verificar si el archivo fue descargado correctamente
    if not os.path.exists(nombre_archivo):
        print("Error: el archivo no se descargó correctamente.")
        return

    # Leer el archivo descargado y copiar al portapapeles
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(contenido)
    win32clipboard.CloseClipboard()

    print("Contenido copiado al portapapeles. Monitoreando cambios...")
    while True:
        time.sleep(2)
        win32clipboard.OpenClipboard()
        nuevo_contenido = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if nuevo_contenido != contenido:
            print("El contenido del portapapeles ha cambiado.")
            break

# Llamada a la función
descargar_y_monitorizar("ftp.scene.org", "welcome.msg")


