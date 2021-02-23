import math

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
d = min(a,b)

while True:
  if(a % d == 0 and b % d == 0):
    gcd = d 
    break
  d = d - 1
print("GCD is", gcd)