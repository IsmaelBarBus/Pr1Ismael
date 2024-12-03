import threading
import time

# Crear un evento
llegado_corredor = threading.Event()

def corredor(id_corredor):
    print(f"Corredor {id_corredor} en posicion, esperando la señal de salida...")
    llegado_corredor.wait()  # Espera a que la alarma se active
    print(f"Corredor {id_corredor} ha llegado a la meta")

def activar_alarma():
    print("Señal de salida en 2 segundos...")
    time.sleep(2)  # Simular tiempo antes de activar la alarma
    llegado_corredor.set()  # Activa el evento, permitiendo que todos los sensores continúen
    print("Salida! Los corredores han comenzado")

# Crear e iniciar hilos para 5 sensores
corredores = []
for i in range(5):
    t = threading.Thread(target=corredor, args=(i,))
    corredores.append(t)
    t.start()

# Activar la alarma después de un tiempo
salida = threading.Thread(target=activar_alarma)
salida.start()

# Esperar a que todos los hilos terminen
for t in corredores:
    t.join()
salida.join()

