from time import perf_counter
import re

def solve(pos, end, c):
    done = set()
    q = [(pos, 0, [pos])]
    while q:
        q.sort(key=lambda x: x[1])
        pos, d, path = q.pop(0)
        if pos in c or pos in done: continue
        if pos == end: return d, path
        done.add(pos)
        for m in (1+0j, -1+0j, 0+1j, 0-1j):
            newpos = pos + m
            if 0 <= newpos.real < end.real + 1 and 0 <= newpos.imag < end.imag + 1:
                q.append((newpos, d + 1, path + [newpos]))
    return -1, []

def main():
    corrupted = [(int(x) + int(y)*1j) for x, y in re.findall("(\d+),(\d+)", open("18.txt").read())]
    p1, p2 = 0, 0
    end = 70+70j
    pos = 0+0j
    B = 1024
    C = corrupted[:B]
    p1, path = solve(pos, end, C)
    while B < len(corrupted):
        if corrupted[B] in path:
            d, path2 = solve(pos, end, C)
            if d == -1:
                p2 = ','.join(str(i) for i in (int(C[-1].real), int(C[-1].imag)))
                break
            path = path2
        B += 1
        C.append(corrupted[B])
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    