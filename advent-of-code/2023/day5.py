with open("input/day5.txt", "r") as f:
    test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    seeds, *maps = test.split("\n\n")
    seeds = [int(x) for x in seeds.split(": ")[1].split()]

    #  seeds, *maps = f.read().strip().split("\n\n")
    #  seeds = [int(x) for x in seeds.split(": ")[1].split()]

print(seeds)


def parse_map(mapstr):
    lines = mapstr.split("\n")[1:]
    output = []
    for line in lines:
        dest, src, delta = line.split()
        output.append((int(src), int(dest), int(delta)))

    return sorted(output)


def get_dest(src, parsed_map):
    dest = src
    for line in parsed_map:
        if src in range(line[0], line[0] + line[2]):
            dest = src - line[0] + line[1]

    return dest


for m in maps:
    seeds = [get_dest(s, parse_map(m)) for s in seeds]


print(min(seeds))
