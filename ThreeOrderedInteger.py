'''
Read three integers from the keyboard a,b,c and those values in the following order.
max > mid > min

Sample Input 
10 1 7

Sample Output
10 > 7 > 1
'''

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

x = max(a,b,c)
y = min(a,b,c)
z = (a+b+c)-x-y

print(x,z,y,sep=">")
