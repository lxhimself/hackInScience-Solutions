import math

n = int(input("Give me a number: "))


def is_prime(n):
  if n != 1:
    for i in range(2, int(math.sqrt(n) +1)):
        if ((n%i) == 0):
            return False
    return True
  else:
     return False


print(is_prime(n))


