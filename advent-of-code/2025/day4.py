with open("input/day4.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]

dirs = {'LU': (-1, -1),
        'L': (0, -1),
        'LD': (1, -1),
        'U': (-1, 0),
        'D': (1, 0),
        'RU': (-1, 1),
        'R': (0, 1),
        'RD': (1, 1) }

def is_acc(i, j):
    n=0
    for d in dirs.values(): 
        ni = i+d[0]
        nj = j+d[1]

        if ni<0 or ni>len(inputs)-1 or nj<0 or nj>len(inputs[0])-1:
            pass
        elif inputs[ni][nj] == '.':
            pass
        else:
            n+=1

    return True if n<4 else False

rounds = []

while True:
    acc=0
    inputs1 = []
    for i, row in enumerate(inputs):
        t = ''
        for j, col in enumerate(row):
            if col == '@' and is_acc(i, j):
                t+='.'
                acc+=1
            else:
                t+=col

        inputs1.append(t)

    rounds.append(acc)
    inputs = inputs1
    if acc <= 0:
        break

print(rounds[0], sum(rounds))

