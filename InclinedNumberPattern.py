'''
PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.

Input Format
A SINGLE INTEGER DENOTING N VALUE

Constraints
1<=N<=100

Output Format
PATTERN AS SHOWN IN SAMPLE TEST CASE

Sample Input 0
5

Sample Output 0
1
 2
  3
   4
    5
'''

a = int(input("Enter a number: "))

for i in range(a):
    print(" "*i + str(i+1))
