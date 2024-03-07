def power(a, n):
    """
    Calculates the power of a number.

    Parameters:
        a (int): The base number.
        n (int): The exponent.

    Returns:
        int: The result of raising `a` to the power of `n`.
    
    Example:
        >>> power(2, 3)
        8
    """
    ########################
    # Insert your code here:
    #  (replace the underscores)
    #-----------------------    
    if n == 0:
        return 1
    else:
        return int(a * power(a,n-1))