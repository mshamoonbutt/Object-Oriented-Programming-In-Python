def prefix(num, lst):
    # Base case: if the list is empty, do nothing
    if not lst:
        return
    # Print the current element
    # If the current element is equal to num, stop the recursion
    if lst[-1] == num:
        return
    print(lst[-1], end=' ')    
    # Recursive case: call prefix with the rest of the list
    prefix(num, lst[:-1])

# Example usage
prefix(6, [2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44])
