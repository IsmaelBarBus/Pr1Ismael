import psutil

def listar_procesos_activos(nombres_procesos, palabra_clave):
    for proceso in psutil.process_iter(['name', 'pid', 'memory_info']):
        try:
            if any(nombre.lower() in proceso.info['name'].lower() for nombre in nombres_procesos) and palabra_clave.lower() in proceso.info['name'].lower():
                #print(proceso)
                print(f"Proceso: {proceso.info['name']}, PID: {proceso.info['pid']}, Memoria: {proceso.info['memory_info'].rss / 1024 ** 2:.2f} MB")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

nombres_procesos = ["chrome"]
palabra_clave = "chrome"
listar_procesos_activos(nombres_procesos, palabra_clave)
