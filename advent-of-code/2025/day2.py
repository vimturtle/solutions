import re

with open("input/day2.txt", "r") as f:
    inputs = f.read().strip().split(',')

p1, p2 = 0, 0

for inp in inputs:
  start, end = [int(_) for _ in inp.split('-')]
  for n in range(start, end+1):
    s = str(n)
    if s == s[:len(s)//2]*2:
      p1 += n
    #if re.match(r'^(\d+)\1$', str(n)):
      #p1 += n
    if re.match(r'^(\d+)\1+$', str(n)):
      p2 += n

print(p1, p2)

