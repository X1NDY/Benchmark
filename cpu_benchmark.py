import timeit

def cpu_performance():
    test_statement  = """
import math
[math.exp(i) * math.sin(i) for i in range(700)]
"""
    duration=timeit.timeit(test_statement, number=700, globals=globals())
    print(f"La prueba de rendimiento de la CPU tomó {duration:.2f} segundos.")

if __name__ == "__main__":
    cpu_performance()