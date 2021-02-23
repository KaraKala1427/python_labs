import random
x = [random.randint(1, 100) for p in range(1, 101)]
max = x[0]
cnt = 0
for i in range(100):
    if (max < x[i]):
        max = x[i]
        cnt = cnt + 1
        print(x[i] , "<== Update")
    else:
        print(x[i])


print("The maximum value was found {}".format(max))
print("The maximum value was updated {}".format(cnt),"times")
