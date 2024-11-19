import threading

def preparacion(cond):
    for _ in range(5):  # Reduce el número de iteraciones para hacerlo más fácil de seguir
      cont = 0
        with cond:
          cont = cont + 1
            cond.wait()  # Espera a que el otro hilo notifique
            print("preparacion")
            cond.notify()  # Notifica al otro hilo para que continúe

def procesamiento(cond):
    for _ in range(5):
      cont = 0
        with cond:
          cont = cont + 1
            cond.wait()  # Espera a que el otro hilo notifique
            print("procesamiento")
            cond.notify()  # Notifica al otro hilo para que continúe

def empaque(cond):
    for _ in range(5):
      cont = 0
        with cond:
          cont = cont + 1
            cond.wait()  # Espera a que el otro hilo notifique
            print("empaque")
            cond.notify()  # Notifica al otro hilo para que continúe

# Crear una instancia de Condition para coordinar los hilos
cond = threading.Condition()

# Crear e iniciar los hilos
t1 = threading.Thread(target=preparacion, args=(cond,))
t2 = threading.Thread(target=procesamiento, args=(cond,))
t3 = threading.Thread(target=empaque, args=(cond,))
t1.start()
t2.start()
t3.start()

# Iniciar la secuencia con una primera notificación
with cond:
    cond.notify()  # Notifica al primer hilo para que empiece

# Esperar a que ambos hilos terminen
t1.join()
t2.join()
t3.join
