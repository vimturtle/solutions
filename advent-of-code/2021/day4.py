def has_won(board):
    """
    board: 2d array representing a board

    Returns True if the board is solved else False
    """
    return any(all(cell == -1 for cell in row) for row in board) or any(
        all(board[row][col] == -1 for row in range(5)) for col in range(5)
    )


def score(board):
    """
    Calculate total score for a board
    """
    total = 0

    for i in range(5):
        for j in range(5):
            if board["repr"][i][j] != -1:
                total += board["repr"][i][j]

    return total * board["last_num"]


with open("input/day4.txt") as f:
    inputs = f.read().rstrip().split("\n\n")


wins = []
numbers = inputs[0].split(",")
boards = [
    {
        "won": False,
        "repr": [
            [int(cell) for cell in row.strip().split()] for row in board.split("\n")
        ],
    }
    for board in inputs[1:]
]


for n in numbers:
    for b, board in enumerate(boards):
        if not board["won"]:
            found = False
            for i, row in enumerate(board["repr"]):
                for j, cell in enumerate(row):
                    if cell == int(n):
                        found = True
                        board["repr"][i][j] = -1  # Mark the cell
                        break
                if found:
                    break

            if has_won(board["repr"]):
                wins.append({"last_num": int(n), "repr": board["repr"]})
                boards[b]["won"] = True


print(score(wins[0]), score(wins[-1]))
