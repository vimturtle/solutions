# This problem can easily be solved using the standard library
# but I have also done it using only the information given to us

# from calendar import weekday
# 
# print(sum(weekday(y, m, 1) == 6 
#           for y in range(1901, 2001) 
#           for m in range(1, 13)))

# --- or ---

# from datetime import date
# 
# print(sum(date(y, m, 1).weekday() == 6
#           for y in range(1901, 2001) 
#           for m in range(1, 13)))

# ----------

is_leap = lambda y: (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def num_days(m, year):
    # Return the number of days in month m, 0=Jan, 11=Dec
    if m == 1:
        return 29 if is_leap(year) else 28
    return 30 if m in [3, 5, 8, 10] else 31

jan_1900 = 1 # Monday
jan_1901 = ((366 if is_leap(1900) else 365) + jan_1900) % 7

curr = jan_1901
sundays = 0

for y in range(1901, 2001):
    for m in range(0, 12):
        if curr == 0:
            sundays += 1
        curr = (num_days(m, y) + curr) % 7

print(sundays)
