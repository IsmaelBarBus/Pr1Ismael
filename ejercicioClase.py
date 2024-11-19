import threading

def preparacion(cond):
    for _ in range(5): 
      cont = 0
        with cond:
          cont = cont + 1
            cond.wait()
            print("preparacion" + cont + "completado")
            cond.notify()

def procesamiento(cond):
    for _ in range(5):
      cont = 0
        with cond:
          cont = cont + 1
            cond.wait()  
            print("procesamiento" + cont + "completado")
            cond.notify()  

def empaque(cond):
    for _ in range(5):
      cont = 0
        with cond:
          cont = cont + 1
            cond.wait()
            print("empaque" + cont + "completado")
            cond.notify()

cond = threading.Condition()

t1 = threading.Thread(target=preparacion, args=(cond,))
t2 = threading.Thread(target=procesamiento, args=(cond,))
t3 = threading.Thread(target=empaque, args=(cond,))
t1.start()
t2.start()
t3.start()

with cond:
    cond.notify() 

t1.join()
t2.join()
t3.join()
