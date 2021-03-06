# 1. Compound Interest
principal = float(input("Enter principle amount : Rs. "))
rate = float(input("Enter the rate (%): "))
time = float(input("Enter the time (years): "))

amt = principal * (1 + rate / 100) ** time
interest = amt - principal

print('Total interest amount is: Rs. ', round(interest, 2))
print('Total amount is: Rs. ', round(amt, 2))
