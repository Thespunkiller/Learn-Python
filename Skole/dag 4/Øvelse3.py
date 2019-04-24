def if_different(data) :
    
  if len(data) == len(set(data)):
    return True
  else:
    return False

#print(if_different([1,5,7,9]))
#print(if_different([2,4,5,5,7,9]))



