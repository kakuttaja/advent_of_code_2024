from collections import deque
from time import perf_counter

def is_valid(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

def get_corners(y, x, grid):
    def get_value(y, x):
            return grid[y][x] if 0 <= y < len(grid) and 0 <= x < len(grid[0]) else "."
    corners = 0
    l = grid[y][x]
    n = [
        get_value(y-1,x),
        get_value(y,x+1),
        get_value(y+1,x),
        get_value(y,x-1)
    ]
    d = [
        (get_value(y-1,x-1), n[0], n[3]),
        (get_value(y-1,x+1), n[0], n[1]),
        (get_value(y+1,x+1), n[2], n[1]),
        (get_value(y+1,x-1), n[2], n[3])
    ]
    corners += sum([n[i] != l and n[(i + 1) % 4] != l for i in range(4)])
    corners += sum([diag != l and s1 == l and s2 == l for diag, s1, s2 in d])
    return corners

def main():
    grid = [list(row) for row in open("12.txt").read().strip().split()]
    done = set()
    vals = []
    p1, p2 = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            l = grid[i][j]
            if (i, j) in done: continue
            q = deque([(i, j)])
            k = len(vals)
            while q:
                (y, x) = q.popleft()
                if (y, x) in done: continue
                if k == len(vals): vals.append([1, 0, 0])
                else: vals[k][0] += 1
                vals[k][2] += get_corners(y, x, grid)
                done.add((y, x))
                for dir in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    newy, newx = y + dir[0], x + dir[1]
                    if is_valid(newy, newx, grid):
                        l2 = grid[newy][newx]
                        if l2 == l:
                            q.append((newy, newx))
                            continue
                    vals[k][1] += 1
    for (a, p, c) in vals:
        p1 += a * p
        p2 += a * c
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    