from time import perf_counter
import re

def do_step(robots, x, y):
    for i in range(len(robots)):
        p, v = robots[i]
        newx = v[0] + p[0]
        newy = v[1] + p[1]
        if newx < 0:
            newx = x + newx
        else:
            newx %= x
        if newy < 0:
            newy = y + newy
        else:
            newy %= y
        robots[i] = [[newx, newy], v]
    return robots

def get_safety_level(robots, midx, midy):
    q = [0, 0, 0, 0]
    for p, _ in sorted(robots, key=lambda x: x[0]):
        j, i = p
        if j == midx: continue
        if i == midy: continue
        if i < midy and j < midx:
            q[0] += 1
        elif i < midy and j > midx:
            q[1] += 1
        elif i > midy and j < midx:
            q[2] += 1
        elif i > midy and j > midx:
            q[3] += 1
    v = 1
    for p in q:
        v *= p
    return v

def main():
    robots = []
    with open("14.txt") as f:
        for line in f.read().strip().split('\n'):
            (a, b), (c, d) = re.findall("(-?\d+),(-?\d+)", line)
            p = (int(a), int(b))
            v = (int(c), int(d))
            robots.append([p,v])
    steps = 0
    x, y = 101, 103
    midx = x // 2
    midy = y // 2
    sets = {}
    for _ in range(100):
        steps += 1
        robots = do_step(robots, x, y)
        sets[steps] = (robots.copy(), get_safety_level(robots, midx, midy))

    # 
    # The sets can be sorted by order of lowest safety level
    # because the robot density is higher which 
    # likely leads to lower total quartile products
    # 
    # Then the timestep can be visually ascertained.
    # For this input it was the first timestep to be printed for range(10000).
    # 

    # with open("14_1.txt", "w") as f:
    #     for n in sorted(sets, key=lambda x: sets[x][1]):
    #         f.write(f"{n}\n")
    #         for i in range(y):
    #             for j in range(x):
    #                 if i == midy or j == midx:
    #                     f.write(" ")
    #                     continue
    #                 a = [p for p, v in sets[n][0]]
    #                 if [j,i] not in a:
    #                     f.write(".")
    #                 else:
    #                     f.write(str(a.count([j, i])))
    #             f.write("\n")
    #         f.write("\n")
    return sets[100][1], 8053

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    