from time import perf_counter
from functools import lru_cache

@lru_cache(None)
def rec(num: int, depth: int) -> int:
    if not depth:
        return 1
    if num == 0:
        return rec(1, depth - 1)
    if len(str(num)) % 2 == 0:
        return (rec(int(str(num)[:len(str(num)) // 2]), depth - 1) + 
                rec(int(str(num)[len(str(num)) // 2:]), depth - 1))
    return rec(num * 2024, depth - 1)

def main():
    nums = list(map(int, open("11.txt").read().strip().split()))
    return sum([rec(n, 25) for n in nums]), sum([rec(n, 75) for n in nums])

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    