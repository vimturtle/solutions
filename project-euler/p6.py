n = 100

# https://en.wikipedia.org/wiki/Triangular_number#Formula
# https://en.wikipedia.org/wiki/Square_pyramidal_number#Formula
sq_of_sum = (n * (n + 1) // 2) ** 2
sum_of_sqrs = n * (n + 1) * (2 * n + 1) // 6


print(sq_of_sum - sum_of_sqrs)
