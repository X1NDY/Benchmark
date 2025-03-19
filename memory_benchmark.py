import time

def memory_performance():
    large_list = [i for i in range(1000000)]
    star_time = time.time()

    for i in range(1000000):
        large_list[i]=large_list[i]+1
    
    end_time=time.time()
    print(f"Benchmark de memoria RAM tomó {end_time-star_time:.2f} segundos.")

if __name__ == "__main__":
    memory_performance()