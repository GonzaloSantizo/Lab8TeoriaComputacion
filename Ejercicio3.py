import time

def my_function(n):
    for i in range(1, (n // 3) + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")


start_time = time.time()

# Call the function with a value of n
n_value = 1200  # Replace with your desired value of n
my_function(n_value)

end_time = time.time()
execution_time = end_time - start_time

print(f"Tiempo de ejecución: {execution_time} segundos")