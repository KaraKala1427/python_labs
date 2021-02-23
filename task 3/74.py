print(" ", end="")
for i in range(1,11):
    print(("{:4d}".format(i)), end='')

print()
for i in range(1, 11):
    print(i, end="")
    for j in range(1, 11):
        print(("{:4d}".format(i * j,)), end='')
    print()
 