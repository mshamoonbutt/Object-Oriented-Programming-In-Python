def reverse(s):
    '''
    Reverses the given string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.
    
    Example:
        >>> reverse("hello")
        "olleh"
    '''
    ########################
    # Insert your code here:
    #  (replace the underscores)
    #-----------------------    
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]    