import time

def my_function(n):
    counter = 0
    for i in range(n // 2, n + 1):
        for j in range(1, n - (n // 2) + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

# Línea de inicio de la medición del tiempo
start_time = time.time()

# Call the function with a value of n
n_value = 100  # Reemplaza con el valor de n que desees
result = my_function(n_value)

# Línea de finalización de la medición del tiempo
end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time
print(f"Result: {result}")
print(f"Tiempo de ejecución: {execution_time} segundos")