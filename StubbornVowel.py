'''
In english alphabets there are two types of words, vowels and consonents.You are writing a program to reverse a given string, but the vowels are stubborn to move away from their position. So given a string where the vowels are stubborn,
print what will be word if the entire word is reversed except for the vowels.

Input Format
One string input

Constraints
3<=String length<=10^5

Output Format
Reversed string output

Sample Input 0
missing

Sample Output 0
ngissim

'''

s = input()
a = []
l = []
x = 0

for i in range (len(s)):
    if s[i].lower() in "aeiou":
        a.append(s[i])
        l.append(s[x:i])
        x = i + 1

if s[x:] != "":
    l.append(s[x:])
l.reverse()

rev = ""
for i in range(len(l)):
    if i < len(l):
        rev += l[i]
    if i < len(a):
        rev += a[i]
        
print(rev)
