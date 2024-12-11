# This is the personal finance calculator
# Define variables based on user's input
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

# Annual Interest Rate
interest_rate = 0.05 

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings
projected_savings = (monthly_savings * 12) + (monthly_savings*12*interest_rate)

# Print the monthly savings, and projected annual savings including interest
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is ${projected_savings}.")