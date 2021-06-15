'''
Read three integers from the keyboard a,b,c, d and those values in the following order.
max > mid1 > mid2 > min

Sample Input 
10 1 7 5

Sample Output
10 > 7 > 5 > 1
'''

a,b,c,d = map(int, input("Enter 4 numbers: ").split())

w = max(a,b,c,d)
x = min(a,b,c,d)
z = (a+b+c+d)-w-x

if a+b == z:
    y = min(a,b)
elif a+c == z:
    y = min(a,c)
elif a+d == z:
    y = min(a,d)
elif b+c == z:
    y = min(b,c)
elif b+d == z:
    y = min(b,d)
elif c+d == z:
    y = min(c,d)

s = z-y

print(w,s,y,x, sep=">")
