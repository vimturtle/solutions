#  with open("input/gc.txt") as f:
#  s1, s2 = f.read().splitlines()
#  print(sum([a != b for a, b in zip(s1, s2)]))

test = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

lines = test.splitlines()

highest_gc = 0
highest_id = ""

for i, line in enumerate(lines):
    if not line.startswith(">"):
        gc = [c for c in line if c in ["C", "G"]]
        gc_content = len(gc) * 100 / len(line)

        if gc_content > highest_gc:
            highest = gc_content
            highest_id = lines[i - 1]

print(highest_id + "\n" + highest_gc)
