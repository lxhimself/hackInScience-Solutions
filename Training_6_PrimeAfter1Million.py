import math


def is_prime(n):
  if n != 1:
    for i in range(2, int(math.sqrt(n) +1)):
        if ((n%i) == 0):
            return False
    return True
  elif n == 2:
    return True
  else:
     return False
  
  
  
def nextprime(is_prime):
    
  prime = False
  i = 100_000_000

  while prime == False:
    if is_prime(i) is True:
        print(i)
        break
    elif is_prime(i) is False:
        i +=1



nextprime(is_prime)



