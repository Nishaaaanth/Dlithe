'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given N scores. Store them in a list and find the score of the runner-up.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5
'''

n = int(input())
s = list(map(int, input().split()))

if n > len(s) or n < len(s):
    print("Enter the number of scores properly!")
else:
    x = s.count(max(s))
    for i in range(x):
        s.remove(max(s))
    print(max(s))
