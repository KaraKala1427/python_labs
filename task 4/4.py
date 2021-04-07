n,m,a = map(int,input().split()) 
if m%a == 0: 
 k = m//a 
else: 
 k = m//a+1 
  
if n%a == 0: 
 p = n//a 
else: 
 p = n//a+1 
  
print(k*p) 