def Sum(lst):
    """
    Calculates the sum of all the elements in the given list.

    Parameters:
        lst (list): A list of numbers.

    Returns:
        int: The sum of all the elements in the list.

    Example:
        >>> Sum([5, 2, 9, 1, 7])
        24
    """
    ########################
    # Insert your code here:
    #  (replace the underscores)
    #-----------------------    
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + Sum(lst[1:])  
    
print(Sum([5,2,9,1,7]))   