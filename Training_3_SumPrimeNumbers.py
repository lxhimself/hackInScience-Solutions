import math

n = int(input("Give me a number: "))





def is_prime(n)
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
    
  summe = 0

  for i in range(1, n):
    if is_prime(i) is True:
        summe += i
  return summe


print(sum_primes(is_prime))




