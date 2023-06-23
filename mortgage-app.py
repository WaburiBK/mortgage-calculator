principal = 100000
interest = 7.5
years = 30

# convert years to months
months = years * 12

# convert interest rate to monthly interest rate
monthly_interest_rate = interest / (12 * 100)

# calculate monthly payment using formula for fixed monthly payments
monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months)))

print(f"For a {years}-year mortgage loan of ${principal} at an annual interest rate of {interest:.2f}% you pay ${monthly_payment:.2f} each month.")