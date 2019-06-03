annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("Enter the cost of your dream home: ")

yearly_savings = float(annual_salary) * float(portion_saved)
monthly_savings = yearly_savings / 12
goal = float(total_cost)