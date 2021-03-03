def triangle(a, b, c): 
    lenghts = [a,b,c]
    lenghts.sort()
    if lenghts[2] < (lenghts[1] + lenghts[0]):
        return True
    else: 
        return False

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if triangle(a, b, c): 
    print("Yes, it is possible to form triangle")
else: 
    print("No, it is impossible to form triangle")