from time import perf_counter
from collections import defaultdict
from itertools import combinations
import re
import numpy as np

def main():
    p1, nodes = 0, defaultdict(set)
    for (n1, n2) in re.findall('(\w\w)-(\w\w)', open("23.txt").read().strip()):
        nodes[n1].add(n2)
        nodes[n2].add(n1)
    for n1, n2, n3 in combinations(nodes, 3):
        if not (n2 in nodes[n1] and n3 in nodes[n1] and n3 in nodes[n2]): continue
        if 't' in (n1+n2+n3)[::2]: p1 += 1
    networks = [{c} for c  in nodes]
    for net in networks:
        for node, neighbours in nodes.items():
            if net.issubset(neighbours):
                net.add(node)
    return p1, ','.join(sorted(max(networks, key=len)))

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    