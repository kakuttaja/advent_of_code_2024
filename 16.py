from time import perf_counter

def is_valid(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] != "#"

def best_path(grid, start):
    done = {}
    q = []
    q.append((start, 0, (0, 1), [start]))
    best = float('inf')
    p2 = set()
    while q:
        q = sorted(q, key=lambda x: x[1])
        (y, x), d, dir, path = q.pop(0)
        if d <= done.get((y, x, dir), float('inf')):
            done[(y, x, dir)] = d
        else: continue
        if d > best: continue
        if grid[y][x] == "E":
            best = d
            for p in path:
                p2.add(p)
            continue
        for (dy, dx) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = y + dy, x + dx
            if is_valid(ny, nx, grid):
                if (dy, dx) in path: continue
                if (dy, dx) != dir:
                    q.append(((ny, nx), d + 1001, (dy, dx), path + [(ny, nx)]))
                else:
                    q.append(((ny, nx), d + 1, (dy, dx), path + [(ny, nx)]))
    return best, len(p2)

def main():
    p1, p2 = 0, 0
    grid = [[j for j in i] for i in open("16.txt").read().strip().split('\n')]
    start = (len(grid) - 2, 1)
    p1, p2 = best_path(grid, start)
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")