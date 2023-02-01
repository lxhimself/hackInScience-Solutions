import math

n = 7

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
  
  
  
def sum_primes(is_prime):
    
  liste = []

  for i in range(10000, 10050):
    if is_prime(i) is True:
        liste.append(i)
  print(*liste, sep = ', ')



sum_primes(is_prime)
