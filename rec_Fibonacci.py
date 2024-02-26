def fibonacci(x):
    if x<=0:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(5))    