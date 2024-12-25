from time import perf_counter
import numpy as np

def main():
    schematics = []
    with open("25.txt") as f:
        for shape in f.read().split('\n\n'):
            s = [[j for j in i] for i in shape.split()]
            schematics.append(s)
    keys, locks = [], []
    for s in schematics:
        if "." in s[0]:
            keys.append(s)
        else:
            locks.append(s)
    p1, p2 = 0, 0
    keys, locks = np.array(keys), np.array(locks)
    keys = keys == "#"
    locks = locks == "#"
    keynums = []
    locknums = []
    for key in keys:
        x = []
        for j in range(len(key[0])):
            # print(key[:,j])
            for i, c in enumerate(key[:,j]):
                if c == True:
                    x.append(5 - (i - 1))
                    break
        keynums.append(x)
    for lock in locks:
        x = []
        for j in range(len(lock[0])):
            # print(lock[:,j])
            for i, c in enumerate(lock[:,j]):
                if c == False:
                    x.append(i - 1)
                    break
        locknums.append(x)
    for key in keynums:
        for lock in locknums:
            key = np.array(key)
            lock = np.array(lock)
            r = key + lock
            if np.all(key + lock <= 5):
                p1 += 1
    return p1,

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")