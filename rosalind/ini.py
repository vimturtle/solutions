with open("input/ini.txt", "r") as f:
    dna = f.read()
    print(" ".join([str(dna.count(c)) for c in ["A", "C", "G", "T"]]))
