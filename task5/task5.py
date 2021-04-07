#question 1
a = {4, 3.3, 8,'d'}
b= set([1,'b',6.9])
print(a)
print(b)

#question 2
a = {4, 3.3, 8,'d'}
for i in a:
    print(i)

#question 3
a = {4, 3.3, 8,'d'}
a.add('a')
b = {1,2,'c'}
a.update(b)
print(a)

#question 4
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
a.remove('d')
a.discard(0)
a.pop()
print(a)

#question 5
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
a.discard(4)
print(a)

#question 6
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
print(a&b)

#question 7
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
print(a|b)

#question 8
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
print(a-b)

#question 9
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
U = a|b
I = a&b
print(U-I)

#question 10
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
c = {2, 'a'}

print("If b is the subset of a")
print(b.issubset(a))
print("If c is the subset of a")
print(c.issubset(a))

#question 11
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
c = a.copy()
print(c)

#question 12
b = {'a', 4 , 7,'g'}
b= b.clear()
print(b)

#question 13
b = {'a', 4 , 7,'g'}
c = frozenset(b)
print(c)

#question 14
def maximum(a):
    return (max(a))
def minimum(a):
    return (min(a))

a = {1, 2, 5, 3, 9, 91, 44.4, 8.77}
print("Max value = ", maximum(a))
print("Min value = ", minimum(a))

#question 15
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
l = len(a)
print("Length of a set = ", l)

#question 16
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
print('d' in a)
print(7 in a)

#question 17
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
if(a&b==set()):
    print("NO element in common")
else:
    print(a&b)

#question 18
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g',6}
c = {'a', 4 , 7,'g'}
print(a.issuperset(b))
print(a.issuperset(a))
print(b.issuperset(c))

#question 19
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
print(a-b)

#question 20
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'t', 55 , 7,'g'}
if(a&b==set()):
    print("sets a and b have no elements in common")
else:
    print("common elements: ", a&b)

#question 21
a = {1, 2, 'a', 4, 8, 3.3, 'd', 'c'}
b = {'a', 4 , 7,'g'}
I = a&b
print(a-I)