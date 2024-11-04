from multiprocessing import Process, Pipe

def proceso_hijo(conn):
    # Recibir contenido del archivo enviado por el proceso padre
    contenido_completo = ""
    while True:
        contenido = conn.recv()  # Recibir fragmentos de datos
        if contenido == "END":   # Señal de fin de transmisión
            break
        contenido_completo += contenido
    
    # Calcular líneas y palabras
    lineas = contenido_completo.count('\n')
    palabras = len(contenido_completo.split())
    print(f"Hijo: {lineas+1} líneas, {palabras} palabras")
    conn.close()

def intercambio_archivo_pipe(ruta_archivo):
    # Crear un pipe para comunicación entre procesos
    padre_conn, hijo_conn = Pipe()

    # Crear proceso hijo
    proceso = Process(target=proceso_hijo, args=(hijo_conn,))
    proceso.start()

    # Leer y enviar contenido del archivo en fragmentos
    with open(ruta_archivo, 'r') as archivo:
        while True:
            fragmento = archivo.read(1024)  # Leer en fragmentos de 1024 bytes
            if not fragmento:
                break
            padre_conn.send(fragmento)

    # Enviar señal de finalización de transmisión
    padre_conn.send("END")

    # Esperar a que el proceso hijo termine
    proceso.join()

if __name__ == '__main__':
    intercambio_archivo_pipe("texto.txt")

