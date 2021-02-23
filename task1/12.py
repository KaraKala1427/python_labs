import math
x1, y1 = float(input("Enter the first longitude point = ")), \
         float(input("Enter the second longitude point = "))
x2, y2 = float(input("Enter the first latitude point = ")), \
         float(input("Enter the second latitude point = "))
t1 = 0.017*x1
g1 = 0.017*y1
t2 = 0.017*x2
g2 = 0.017*y2
print("Distance between two points on the surface of Earth = ",
      round(6371.01*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2)), 2))