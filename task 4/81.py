import math as m

def pithagorean(a, b):
    hypotenuse = m.sqrt(a**2 + b**2)
    return hypotenuse


catet_a = float(input("Enter A: "))
catet_b = float(input("Enter B: "))

print(pithagorean(catet_a, catet_b))