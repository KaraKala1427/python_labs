print("Pribe = $1")
print("Shopper`s money: ")
b = int(input())
# b = (100 - int(b));
d = 10
n = 5
q = 25
t = 200
l = 100
nd = 0
nn = 0
nq = 0
nt = 0
nl = 0

if b >=200:
    nt = int(b/t)
    b = b%t
if b >=100:
    nl = int(b/l)
    b = b%l
if b >=25:
    nq = int(b/q)
    b = b%q
if b >=10:
    nd = int(b/d)
    b = b%d
if b >=5:
    nn = int(b/n)
    b = b%n
print("So the boints are", nt, "toonies, ", nl, "loonies, ", nq, "quarters, ", nd, "dimes, ", nn, " nickels, ",b, " pennies" )

