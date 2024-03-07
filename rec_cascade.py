def cascade(s):
    
    ########################
    # Insert your code here:
    #-----------------------  
    if len(s) == 1:
        print(s)
    else:
        print(s)
        cascade(s[:-1])  
        print(s)       