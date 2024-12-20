from time import perf_counter
from collections import deque, defaultdict

def is_valid(y, x, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])

def main():
    grid = [list(map(int, l)) for l in open("10.txt").read().strip().split()]
    for P2 in (False, True):
        q = deque([((y, x), [(y, x)]) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == 0])
        trails = defaultdict(list)
        while q:
            (i, j), path = q.popleft()
            if grid[i][j] == 9:
                if P2:
                    if tuple(path) in trails[path[0]]: continue
                    trails[path[0]].append(tuple(path))
                else:
                    if path[-1] in trails[path[0]]: continue
                    trails[path[0]].append(path[-1])
                continue
            for y, x in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if is_valid(i + y, j + x, grid) and grid[i + y][j + x] == grid[i][j] + 1:
                    q.append(((i + y, j + x), path + [(i + y, j + x)]))
        if not P2:
            p1 = sum(len(trails[i]) for i in trails.keys())
        else:
            p2 = sum(len(trails[i]) for i in trails.keys())
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")