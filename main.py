#importaciones
from cpu_benchmark import cpu_performance    
from memory_benchmark import memory_performance
from disk_benchmark import disk_performance

#menu
def menu():
    print("Selecciona una prueba de benchmark: ")
    print("1. Procesador")
    print("2. Memoria RAM")
    print("3. Disco Almacenamiento")
    print("4. Informacion del sistema")
    print("5.- Salir")
    choice = input("Selecciona una opcion: ")

    if choice =="1":
        cpu_performance()
    elif choice =="2":
        memory_performance()
    elif choice =="3":
        disk_performance()
    
if __name__ == "__main__":
    menu()