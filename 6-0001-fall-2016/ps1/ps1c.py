annual_salary = float(input("Enter the starting salary: "))
semi_annual_raise = 0.07
return_perc = 0.04
portion_down_payment = 0.25
total_cost = 1000000
num_months = 36
total_down_payment = portion_down_payment*total_cost

num_guesses = 0
epsilon = 100
low, high = 0, 10000
guess = int((low+high)/2)


def calculate_savings(portion_saved, annual_sal=annual_salary):
    """
    Returns total savings after 36 months at portion_saved rate
    """
    current_savings = 0
    for n in range(1, num_months+1):
        if n % 6 == 0 and n != 0:
            annual_sal += annual_sal * semi_annual_raise

        current_savings += (portion_saved/10000 * annual_sal / 12) + \
            (current_savings * return_perc) / 12
    return current_savings


if calculate_savings(high) < total_down_payment:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs(calculate_savings(guess) - total_down_payment) >= epsilon:
        num_guesses += 1
        if calculate_savings(guess) < total_down_payment:
            low = guess
        else:
            high = guess
        guess = int((low+high)/2)
    print("Best savings rate: ", guess/10000)
    print("Steps in bisection search: ", num_guesses)
