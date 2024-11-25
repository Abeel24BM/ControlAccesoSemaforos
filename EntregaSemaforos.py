import threading
import time
import random

capacidad_maxima = 3
semaforo = threading.Semaphore(capacidad_maxima)

# Función que simula el acceso y salida de un vehículo
def acceder_estacionamiento(id_vehiculo):
    print(f"Vehículo {id_vehiculo} está intentando acceder al estacionamiento.")
    semaforo.acquire()
    try:
        print(f"Vehículo {id_vehiculo} ha entrado al estacionamiento.")
        tiempo_estacionamiento = random.uniform(1, 3)
        time.sleep(tiempo_estacionamiento)
    finally:
        print(f"Vehículo {id_vehiculo} ha salido del estacionamiento.")
        semaforo.release()

# Crear e iniciar los hilos para los vehículos
hilos = []
numero_vehiculos = 10

for i in range(numero_vehiculos):
    hilo = threading.Thread(target=acceder_estacionamiento, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Todos los vehículos han pasado por el estacionamiento.")
