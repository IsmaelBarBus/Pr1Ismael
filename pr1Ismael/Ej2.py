from threading import Thread, local
import time


sesion = local()

def iniciar_sesion(nombre):
    sesion.usuario = nombre
    print(f"Sesión iniciada para {sesion.usuario}")
    realizar_acciones()

def realizar_acciones():
    print(f"Usuario {sesion.usuario} está realizando acciones...")
    time.sleep(1)
    cerrar_sesion()

def cerrar_sesion():
    print(f"Sesión cerrada para {sesion.usuario}")
    del sesion.usuario

hilos = [
    Thread(target=iniciar_sesion, args=("Alice",)),
    Thread(target=iniciar_sesion, args=("Bob",)),
    Thread(target=iniciar_sesion, args=("Charlie",))
]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()
