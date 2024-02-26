def sumOfDigits(x):
    if x < 10:
        return x
    else:
        return x % 10 + sumOfDigits(x//10)
print(sumOfDigits(12345))