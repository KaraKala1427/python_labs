
def prime_factorization(n):
    factor = 2
    n = int(n)
    while factor <= n: 
        if n%factor == 0:
            print(factor)
            n = n//factor
            # print("n",n)
        else: 
            factor = factor + 1

number = input("Enter an integer(2 or greater): ")

print(prime_factorization(number))