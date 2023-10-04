def my_function(n):
    counter = 0
    for i in range(n // 2, n + 1):
        for j in range(1, n - (n // 2) + 1):
            k = 1
            while k <= n:
                counter += 1
                k *= 2
    return counter

# Call the function with a value of n
n_value = 100  # Replace with your desired value of n
result = my_function(n_value)
print(f"Result: {result}")
