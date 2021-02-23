a = int(input())
sum=0
i=1
while(i<=4):
    sum=int(sum+int(a%10))
    a=int(a/10)
    i=i+1

print(sum)



