with open("input/dna.txt") as f:
    print(*map(f.read().strip().count, "ACGT"))
