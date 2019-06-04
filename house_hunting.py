portion_down_payment = .25
current_savings = 0
r = .04
months = 0

annual_salary_as_str = input("Enter your annual salary: ")
portion_saved_as_str = input(
    "Enter the percent of your salary to save, as a decimal: ")
total_cost_as_str = input("Enter the cost of your dream home: ")
annual_salary = int(annual_salary_as_str)
portion_saved = float(portion_saved_as_str)
total_cost = int(total_cost_as_str)
down_payment = total_cost / portion_down_payment

if annual_salary > 0:
    monthly_savings = (annual_salary / 12) * portion_saved

else:
        print("You have no income, buddy.")

while current_savings < down_payment:
    months += 1
    current_savings += monthly_savings + (current_savings * (r / 12))

print("Number of months:", str(months))