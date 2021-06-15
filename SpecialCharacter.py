'''
Program to check if a string contains any special character
Given a string, the task is to check if that string contains any special character (defined special character set). If any special character found, don’t accept that string.

Examples :

Input : Python$For$Developers
Output : String is not accepted.

Input : Python For Developers
Output : String is accepted
'''

a = input()

for i in a:
    if not i.isalnum():
        b = True
    else:
        b = False

if b == False:
    print("String is accepted")
else:
    print("String is not accepted")
