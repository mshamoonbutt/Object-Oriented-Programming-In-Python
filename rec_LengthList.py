def LengthList(lst):
    if lst == []:
        return 0        
    else:
        return LengthList(lst[1:]) + 1
print(LengthList([1,2,3,4,5])) 