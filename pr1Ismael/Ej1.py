from threading import Thread, Lock
import time

usuarios = []
lock = Lock()

def agregar_usuario(nombre, edad, **kwargs):
    with lock:
        usuarios.append({"nombre": nombre, "edad": edad, **kwargs})
        print(f"Usuario {nombre} agregado.")

def eliminar_usuario(nombre):
    with lock:
        for user in usuarios:
            if user["nombre"] == nombre:
                usuarios.remove(user)
                print(f"Usuario {nombre} eliminado.")
                return
        print(f"Usuario {nombre} no encontrado.")

def mostrar_usuarios():
    with lock:
        print("Lista de usuarios:")
        for user in usuarios:
            print(user)
        print("")

hilos = [
    Thread(target=agregar_usuario, args=("Alice", 30), kwargs={"email": "alice@example.com"}),
    Thread(target=agregar_usuario, args=("Bob", 25), kwargs={"email": "bob@example.com"}),
    Thread(target=mostrar_usuarios),
    Thread(target=eliminar_usuario, args=("Alice",)),
    Thread(target=mostrar_usuarios)
]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()
