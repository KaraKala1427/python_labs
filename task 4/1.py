n = int(input())
sum = 0

for i in range(n):
    s = input()
    if(s == "Tetrahedron"):
        sum = sum + 4
    elif s == "Cube":
        sum = sum + 6
    elif s == "Octahedron":
        sum = sum + 8
    elif s == "Dodecahedron":
        sum = sum + 12
    elif s == "Icosahedron":
        sum = sum + 20

print(sum)
    
        
