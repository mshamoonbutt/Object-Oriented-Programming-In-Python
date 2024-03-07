def findMin(lst):
    """
    Finds the minimum value in a given list.

    Parameters:
        lst (list): A list of numbers.

    Returns:
        int or float: The minimum value in the list.

    Example:
        >>> findMin([5, 2, 9, 1, 7])
        1
    """
    ########################
    # Insert your code here:
    #-----------------------  
    if len(lst) == 1:
        return lst[0]
    else:
        return min(lst[0], findMin(lst[1:]))     