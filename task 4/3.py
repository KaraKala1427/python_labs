n=int(input())

def f(n):
    sum = 0
    for i in range(1,n+1):
        sum+=i*((-1)**i)
    return sum
    
print(f(n))
