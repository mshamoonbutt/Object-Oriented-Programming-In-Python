def fact(x):
  if x <= 0:    # base case
    return 1
  else:
    return x*fact(x-1)  
print(fact(4))  


# small_result = fact(n-1)
# combined_result = n*small_result
# return combined_result