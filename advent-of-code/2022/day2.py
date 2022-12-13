score1 = score2 = 0


with open("input/day2.txt") as f:
    for game in f.read().splitlines():
        score1 += {"X": 1, "Y": 2, "Z": 3}[game[-1]] + (
            6
            if game in ("A Y", "B Z", "C X")  # Win
            else 3
            if game in ("A X", "B Y", "C Z")  # Draw
            else 0  # Loss
        )

        score2 += {"X": 0, "Y": 3, "Z": 6}[game[-1]] + (
            1
            if game in ("A Y", "B X", "C Z")  # Rock
            else 2
            if game in ("A Z", "B Y", "C X")  # Paper
            else 3  # Scissors
        )


print(score1, score2)
