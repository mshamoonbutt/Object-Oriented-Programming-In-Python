'''def reverse_string(x):
    return x[0] + reverse_string(x[1:])
print(reverse_string("2789"))'''

def reverse_string(string):
    """Reverse a string using recursion."""
    if len(string) == 0:
        return string  # Base case: if the string is empty, return it
    else:
        return reverse_string(string[1:]) + string[0]  # Recursive case: reverse the substring starting from the second character and append the first character

# Example usage:
input_string = "Hello, world!"
reversed_string = reverse_string(input_string)
print(f"The original string: {input_string}")
print(f"The reversed string: {reversed_string}")
