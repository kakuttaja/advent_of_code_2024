from time import perf_counter

def f(r):
    if sorted(r) != r and sorted(r, reverse=1) != r: return False
    for i in range(len(r) - 1):
        if abs(r[i] - r[i + 1]) > 3 or abs(r[i] - r[i + 1]) < 1: return False
    return True

def main():
    nums = [[int(r) for r in n.split()] for n in open("2.txt", "r").read().strip().split('\n')]
    p1 = sum([f(row) for row in nums])
    p2 = sum([any([f(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in nums])
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")