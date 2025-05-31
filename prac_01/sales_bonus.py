"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_BONUS = 0.1
HIGH_BONUS = 0.15
WELL_SALES = 1000

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < WELL_SALES:
        bonus = sales * LOW_BONUS
        print(f"Bonus is {bonus}")
    else:
        bonus = sales * HIGH_BONUS
        print(f"Bonus is {bonus}")
    sales = float(input("Enter sales: $"))
print("Quit")

