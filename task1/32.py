print("Input 3 numbers")
a = int(input())
s = int(input())
d = int(input())

a1 = max(a,s,d)
a2 = min(a,s,d)

print(a2, " ", ((a+s+d) - a1 - a2), " ", a1)



