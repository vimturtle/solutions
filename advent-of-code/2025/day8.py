from math import dist, prod
from itertools import combinations
import networkx as nx  # ver 3.6

with open("input/day8.txt", "r") as f:
    inputs = [line.rstrip() for line in f.readlines()]

coords = [tuple([int(_) for _ in c.split(",")]) for c in inputs]
combs = sorted(list(combinations(coords, 2)), key=lambda c: dist(c[0], c[1]))

G = nx.Graph()
G.add_edges_from(combs[:1000])

print(
    prod(
        [len(_) for _ in sorted(nx.connected_components(G), key=len, reverse=True)][:3]
    )
)

for c in combs[1000:]:
    G.add_edge(c[0], c[1])
    if G.number_of_nodes() == len(coords):
        print(c[0][0] * c[1][0])
        break

