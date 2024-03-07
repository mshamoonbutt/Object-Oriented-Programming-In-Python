def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
input_string = "racecar"
print("Input string:", input_string)
print("Is palindrome:", is_palindrome(input_string))
