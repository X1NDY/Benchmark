import os
import time

def disk_performance():
    file_size_mb = 100
    file_name = "test_file_bin"

    #escritura
    star_time = time.time()
    with open(file_name, "wb") as file: # wb es escribir un archivo binario write
        file.write(os.urandom(file_size_mb *1024 * 1024))
    write_duration = time.time()-star_time

    #lectura
    star_time = time.time()
    with open(file_name, "rb") as file: # rb es leer un archivo binario read
        file.read()
    read_duration = time.time()-star_time

    #borrado
    os.remove(file_name)
    print(f"Tiempo de escritura {write_duration:.2f} segundos.")
    print(f"Tiempo de lectura {read_duration:.2f} segundos.")