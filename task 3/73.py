import string

def is_palindrome(s):
    whitelist = set(string.ascii_lowercase)
    print(whitelist)
    s = s.lower()
    s = ''.join([char for char in s if char in whitelist])
    print(s, s[::-1])
    return s == s[::-1]

s = input("enter:")
if (is_palindrome(s)): 
	print ("Yes")
else: 
	print ("No")