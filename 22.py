from time import perf_counter
from collections import Counter, deque

def main():
    nums = [int(i) for i in open("22.txt").read().strip().split()]
    p1 = 0
    C = Counter()
    for num in nums:
        changes = deque([], maxlen=4)
        prev = num
        sets = set()
        for _ in range(2000):
            num ^= num << 6  & 0xFFFFFF
            num ^= num >> 5  & 0xFFFFFF
            num ^= num << 11 & 0xFFFFFF
            changes.append(num % 10 - prev % 10)
            prev = num % 10
            s = tuple(changes)
            if s not in sets:
                C[s] += num % 10
                sets.add(s)
        p1 += num
    return p1, max(C.values())

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    