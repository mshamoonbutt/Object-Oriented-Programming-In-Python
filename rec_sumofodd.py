def sum_of_odd_index(value, index=0):
    if index >= len(value):
        return 0
    elif index % 2 != 0:
        return int(value[index]) + sum_of_odd_index(value, index + 1)
    else:
        return sum_of_odd_index(value, index + 1)

result = sum_of_odd_index("143219")
print("Sum of odd-indexed values:", result)