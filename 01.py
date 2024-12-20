from time import perf_counter
import numpy as np

def main():
    r = np.loadtxt("1.txt").T
    l, r = sorted(list(map(int, r[0,]))), sorted(list(map(int, r[1,])))
    return (sum(map(lambda a, b: abs(a - b), l, r)), 
            sum([n * r.count(n) for n in l]))


if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")