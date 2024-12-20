from time import perf_counter

def solve(grid, S):
    done = {S: 0}
    q = [S]
    while q:
        pos = q.pop(0)
        for move in (+1, -1, +1j, -1j):
            new = pos + move
            if new in grid and grid[new] != "#" and new not in done:
                done[new] = done[pos] + 1
                q.append(new)
    return done

def main():
    grid = {i+j*1j: c for i,r in enumerate(open("20.txt").read().split())
                      for j,c in enumerate(r)}
    S = [i for i in grid if grid[i] == "S"][0]
    p1, p2 = 0, 0
    distances = solve(grid, S)
    # Get Manhattan distance between two points (max cheat steps)
    # And check if the maze distance between the two points
    # is larger than 100 (the cutoff for cheat gains).
    for k, v in distances.items():
        for k2, v2 in distances.items():
            if k == k2: continue
            dist = abs((k - k2).real) + abs((k - k2).imag)
            if dist == 2  and v - v2 - dist >= 100: p1 += 1
            if dist <= 20 and v - v2 - dist >= 100: p2 += 1
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    