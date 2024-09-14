income = input("Enter your monthly income: ")
expenses = input("Enter your total monthly expenses: ")
savings = float(income) - float(expenses)

Projected_Savings = savings * 12 * 1.05
print(f"Your monthly savings are ${savings}")
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")