annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(
    input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

return_perc = 0.04
portion_down_payment = 0.25

current_savings = 0
num_months = 0
while current_savings < portion_down_payment * total_cost:
    current_savings += (portion_saved * annual_salary / 12) + \
        (current_savings * return_perc) / 12
    num_months += 1

print("Number of months: ", num_months)
