with open("input/revc.txt") as f:
    print(f.read().strip()[::-1].translate(str.maketrans("ACGT", "TGCA")))
