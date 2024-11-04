from multiprocessing import Process, Pipe

def proceso_hijo(conn):
    # Recibir mensaje del proceso padre
    mensaje = conn.recv()
    print(f"Hijo recibió: {mensaje.upper()}")
    conn.send(mensaje.upper())  # Enviar respuesta al padre
    conn.close()

def comunicacion_pipe():
    # Crear un pipe para comunicación entre procesos
    padre_conn, hijo_conn = Pipe()

    # Crear proceso hijo
    proceso = Process(target=proceso_hijo, args=(hijo_conn,))
    proceso.start()

    # Enviar mensaje al hijo
    mensaje = "hola hijo"
    padre_conn.send(mensaje)

    # Recibir respuesta del hijo
    mensaje_modificado = padre_conn.recv()
    print(f"Padre recibió del hijo: {mensaje_modificado}")

    # Esperar a que el proceso hijo termine
    proceso.join()

if __name__ == '__main__':
    comunicacion_pipe()


