import subprocess
import time

def ejecutar_notepad(sincrono=True):
    inicio = time.time()
    if sincrono:
        subprocess.run("notepad.exe")
    else:
        proceso = subprocess.Popen("notepad.exe")
        proceso.wait()
    print(f"Tiempo de ejecución: {time.time() - inicio:.2f} segundos")

modo = input("¿Deseas ejecución síncrona (s) o asíncrona (a)?: ").strip().lower()
ejecutar_notepad(sincrono=(modo == "s"))
