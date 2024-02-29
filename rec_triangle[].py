'''[]
[][]
[][][]
[][][][]'''

def tri(n):
    if n <= 0:
        return
    tri(n-1)
    print("[]"*n)
tri(4)    # you can change the value of n

'''[][][]
[][]
[]'''

def tri(n):
    if n <= 0:
        return
    print("[]"*n)
    tri(n-1)
tri(3)
