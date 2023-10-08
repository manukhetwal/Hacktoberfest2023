def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = 10
for i in range(n_terms):
    print(f"Fibonacci({i}) = {fibonacci(i)}")
