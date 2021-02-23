import math

def isPerfectSquare(x):
   s = int(math.sqrt(x))
   return s*s == x

def isFibonacci(n):
   print(isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4))

isFibonacci(9)
