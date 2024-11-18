from threading import Thread
import os

class ProcesadorArchivo(Thread):
    def __init__(self, archivo, operacion):
        super().__init__()
        self.archivo = archivo
        self.operacion = operacion
        self.resultado = None

    def run(self):
        if not os.path.isfile(self.archivo):
            print(f"El archivo {self.archivo} no existe.")
            return

        with open(self.archivo, 'r') as f:
            contenido = f.read()
            
            if self.operacion == "contar_lineas":
                self.resultado = contenido.count('\n') + 1
            elif self.operacion == "contar_palabras":
                self.resultado = len(contenido.split())
            elif self.operacion == "contar_caracteres":
                self.resultado = len(contenido)
            else:
                print(f"Operación {self.operacion} no reconocida.")
                return

        print(f"Archivo: {self.archivo} | Operación: {self.operacion} | Resultado: {self.resultado}")

hilos = [
    ProcesadorArchivo("archivo1.txt", "contar_lineas"),
    ProcesadorArchivo("archivo2.txt", "contar_palabras"),
    ProcesadorArchivo("archivo3.txt", "contar_caracteres")
]

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()
