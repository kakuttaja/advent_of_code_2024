from time import perf_counter
from collections import deque


def solve(x, p2=False):
    FS, F, D, fid, idx = [], [], [], 0, 0
    for i, n in enumerate(x):
        if i % 2 == 0:
            D.extend([fid] * int(n))
            if p2: 
                FS.append((idx, int(n), fid))
            else: 
                FS.extend([(idx + j, 1, fid) for j in range(int(n))])
            idx += int(n)
            fid += 1
        else:
            F.append((idx, int(n)))
            D.extend([0] * int(n))
            idx += int(n)
    for idx, fsize, fid in reversed(FS):
        for i, (free_idx, space) in enumerate(F):
            if free_idx < idx and fsize <= space:
                D[idx:idx + fsize] = [0] * fsize
                D[free_idx:free_idx + fsize] = [fid] * fsize
                F[i] = (free_idx + fsize, space - fsize)
                break
    return sum(i * n for i, n in enumerate(D))

def main():
    txt = open("9.txt").read().strip()
    return solve(txt, 0), solve(txt, 1)

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    