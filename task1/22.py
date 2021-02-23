import math
s1=int(input("s1:"))
s2=int(input("s2:"))
s3=int(input("s3:"))
s=(s1+s2+s3)/2
Su=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print("The area is: ",Su)