def IsPrime(n):
   d = 2
   while n % d != 0:
       d += 1
   return d == n

def divisors(integer):

    if IsPrime(integer):
        return '{} is prime'.format(integer)
    else:
        return [i for i in range(1, int(integer/2)+1) if integer%i == 0][1:]

print(divisors(122))
