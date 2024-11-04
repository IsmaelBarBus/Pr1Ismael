import psutil


def finalizar_proceso(nombre_proceso):
    for proceso in psutil.process_iter(['name', 'pid']):
        
        try:
            
            if nombre_proceso.lower() in proceso.info['name'].lower():
                proceso.terminate()
                proceso.wait()  # Esperar a que termine
                print(f"Proceso {nombre_proceso} finalizado con éxito.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            print(f"No se pudo finalizar el proceso {nombre_proceso}.")

nombre_proceso = input("Introduce el nombre del proceso a finalizar: ")
finalizar_proceso(nombre_proceso)
