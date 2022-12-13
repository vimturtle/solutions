annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

return_perc = 0.04
portion_down_payment = 0.25

current_savings = 0
num_months = 0
while current_savings < portion_down_payment * total_cost:
    if num_months % 6 == 0 and num_months != 0:
        annual_salary += annual_salary * semi_annual_raise

    current_savings += (portion_saved * annual_salary / 12) + \
        (current_savings * return_perc) / 12
    num_months += 1

print("Number of months: ", num_months)
