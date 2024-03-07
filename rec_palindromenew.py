def isPalindrome(s):
    """
    Check if a string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Example:
        >>> isPalindrome("madam")
        True
    """
    ########################
    # Insert your code here:
    #-----------------------
    x = len(s)
    a = 0
    if x == 1:
        return True
    elif s[a] != s[x-1]:
        return False
    else:
        return isPalindrome(s[a+1:x-1])
    if isPalindrome:
        return True