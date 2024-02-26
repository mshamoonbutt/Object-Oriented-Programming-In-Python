def greatestCommonDiviser(a,b):
    if b == 0:
        return a  
    else:
        return greatestCommonDiviser(b, a % b) 
print(greatestCommonDiviser(44,36))    