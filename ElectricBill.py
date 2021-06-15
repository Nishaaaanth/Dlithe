'''
The tariff rate for all division is the same. Karnataka electricity board single slaps for the domestic LT supply such as for 0 to 30 units the per-unit cost will be ? 3.75/-, from 31 to 100 the per-unit cost will be ? 5.20, from 101 to 200, the per-unit cost will be ? 6.75 and above 201 units you have to pay ? 7.8 per unit.
Additionally, the consumer will pay fixed charges as ? 60/- and electricity tax of 5% extra.
'''

a = int(input("Enter your Electricity Units: "))

if a in range(0,31):
    r = 3.75
elif a in range(31,101):
    r = 5.20
elif a in range(101,201):
    r = 6.75
else:
    r = 7.8

additionalCharge = 60
tax = (5/100)*(a*r)

totalCharge = (a*r)+additionalCharge+tax

print("Electricity Bill: ", “%.2f” %totalCharge)
