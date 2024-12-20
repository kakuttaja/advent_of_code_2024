from functools import lru_cache
from time import perf_counter

@lru_cache(None)
def rec(patterns, design):
    if not design:
        return 1
    res = 0
    for pattern in patterns:
        if len(pattern) <= len(design):
            if design[:len(pattern)] == pattern:
                res += rec(patterns, design[len(pattern):])
    return res

def main():
    patterns, designs = open("19.txt").read().strip().split("\n\n")
    patterns, designs = patterns.replace(' ', '').split(','), designs.split('\n')
    p1, p2 = 0, 0
    for design in designs:
        if res := rec(tuple(patterns), design):
            p1 += 1
            p2 += res
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    