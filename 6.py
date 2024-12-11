from time import perf_counter

def main():
    grid = open("6.txt").read().strip().split()
    p1, p2 = 0, 0
    t = []
    for l in grid:
        t.append([i for i in l])
    grid = t
    for y, l in enumerate(grid):
        if "^" in l:
            pos = (y, grid[y].index("^"))
            dir = 0
    start = pos
    positions = set()
    while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
        old_pos = pos
        grid[pos[0]][pos[1]] = "X"
        if dir == 0:
            pos = (pos[0] - 1, pos[1])
        elif dir == 1:
            pos = (pos[0], pos[1] + 1)
        elif dir == 2:
            pos = (pos[0] + 1, pos[1])
        else:
            pos = (pos[0], pos[1] - 1)
        if not 0 <= pos[0] < len(grid) or not 0 <= pos[1] < len(grid[0]):
            break
        if grid[pos[0]][pos[1]] == "#":
            dir = (dir + 1) % 4
            pos = old_pos
        positions.add(pos)
    p1 = sum(i.count("X") for i in grid)
    done_pos = set()
    for (y, x) in positions:
        done_pos.add((y, x))
        if grid[y][x] not in "#^":
            print(f"{len(done_pos)}/{len(positions)}              ", end="\r")
            grid[y][x] = "#"
            traversed = set()
            pos = start
            dir = 0
            while 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                if (pos, dir) in traversed:
                    p2 += 1
                    break
                traversed.add((pos, dir))
                old_pos = pos
                if dir == 0:
                    pos = (pos[0] - 1, pos[1])
                elif dir == 1:
                    pos = (pos[0], pos[1] + 1)
                elif dir == 2:
                    pos = (pos[0] + 1, pos[1])
                else:
                    pos = (pos[0], pos[1] - 1)
                if not 0 <= pos[0] < len(grid) or not 0 <= pos[1] < len(grid[0]):
                    break
                if grid[pos[0]][pos[1]] == "#":
                    dir = (dir + 1) % 4
                    pos = old_pos
            grid[y][x] = "."
    print("                                           ", end="\r")
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    