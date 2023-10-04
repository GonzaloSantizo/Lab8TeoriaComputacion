def my_function(n):
    for i in range(1, (n // 3) + 1):
        for j in range(1, n + 1, 4):
            print("Sequence")

# Call the function with a value of n
n_value = 12  # Replace with your desired value of n
my_function(n_value)
