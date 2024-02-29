def fibonacci(x):
    if x<=0:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(5))

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(6))  
print(fib(1))
print(fib(2))
print(fib(5))