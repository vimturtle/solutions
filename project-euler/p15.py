import math

R = 20 # right moves
D = 20 # down moves

# To reach bottom right from the top left, we must make
# R+D moves. How many ways are there to arrange R right moves
# (or D down moves) in an R+D long path of right and down moves?

print(math.comb(R + D, R))
# or
# print(math.comb(R + D, D))
