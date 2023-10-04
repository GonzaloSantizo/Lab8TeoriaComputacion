import time

def my_function(n):
    if n <= 1:
        return
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break


start_time = time.time()

# Call the function with a value of n
n_value = 10000  # Replace with your desired value of n
my_function(n_value)
# Línea de finalización de la medición del tiempo
end_time = time.time()

# Calcula el tiempo de ejecución

execution_time = end_time - start_time

print(f"Tiempo de ejecución: {execution_time} segundos")