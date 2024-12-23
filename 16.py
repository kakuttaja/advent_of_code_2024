from time import perf_counter
from heapq import heappop, heappush

def is_valid(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] != "#"

def best_path(grid, start):
    done = {}
    q = []
    heappush(q, (0, start, (0, 1), {start}))
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    best = float('inf')
    p2 = set()
    while q:
        d, (y, x), dir, path = heappop(q)
        if d > best or (y, x, dir) in done and done[(y, x, dir)] < d:
            continue
        done[(y, x, dir)] = d
        if grid[y][x] == "E":
            if d <= best:
                best = d
                p2.update(path)
            continue
        for (dy, dx) in dirs:
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx, grid):
                cost = 1001 if dir != (dy, dx) else 1
                heappush(q, (d + cost, (ny, nx), (dy, dx), path | {(ny, nx)}))
    return best, len(p2)

def main():
    p1, p2 = 0, 0
    grid = [[j for j in i] for i in open("16.txt").read().strip().split('\n')]
    start = (len(grid) - 2, 1)
    p1, p2 = best_path(grid, start)
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")