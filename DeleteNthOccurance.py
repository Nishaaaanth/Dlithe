'''
Python program to remove Nth occurrence of the given word. Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.

Examples:

Input: list - ["Python", "for", "developers", "professionals", "developers"]
       word = developers, N = 2
Output: list - ["Python", "for", "developers", "professionals"]

Input: list - ["can", "you",  "can", "a", "can" "?"]
       word = can, N = 1
Output: list - ["you",  "can", "a", "can" "?"]
'''

l = list(input().split())
s = input()
n = int(input())
c = l.count(s)
x = -1
i = 0

while c>0:
    x = l.index(s,x+1)
    i += 1
    if i == int(n):
        l.pop(x)
        break
    c -= 1

print(l)
