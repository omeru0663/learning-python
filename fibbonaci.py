def fib(n):
    return 1 if n <= 1 else fib(n-1) + fib(n-2)

for n in range(30):
    print(fib(n))