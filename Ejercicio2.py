def my_function(n):
    if n <= 1:
        return
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("Sequence")
            break

# Call the function with a value of n
n_value = 5  # Replace with your desired value of n
my_function(n_value)
