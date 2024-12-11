from collections import defaultdict

def main():
    grid = [list(i) for i in open("8.txt").read().strip().split()]
    p1, p2 = 0, 0
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            l = grid[y][x]
            if l != ".":
                antennas[l].append((y, x))
    antinodes = set()
    ans = [0, 0]
    for P2 in (False, True):
        for _, positions in antennas.items():
            n = len(positions)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    y1, x1 = positions[i]
                    y2, x2 = positions[j]
                    x3 = x2 + (x2 - x1)
                    y3 = y2 + (y2 - y1)
                    if P2:
                        antinodes.add((y2, x2))
                        while 0 <= x3 < len(grid[0]) and 0 <= y3 < len(grid[1]):
                            antinodes.add((y3, x3))
                            x3 += (x2 - x1)
                            y3 += (y2 - y1)
                    else:
                        if 0 <= x3 < len(grid[0]) and 0 <= y3 < len(grid[1]):
                            antinodes.add((y3, x3))
                            grid[y3][x3] = "#"
        ans[P2] = len(antinodes)
    return tuple(ans)

if __name__ == '__main__':
    print(main())
    