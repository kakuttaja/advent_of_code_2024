from time import perf_counter
import re

def main():
    sets = {}
    for line in open("13.txt").read().strip().split("\n\n"):
        nums = list(map(int, re.findall(r"\d+", line)))
        sets[tuple(nums[-2:])] = nums[:2], nums[2:4]
    res = [0, 0]
    for P2 in range(2):
        for (Tx, Ty), ((Ax, Ay), (Bx, By)) in sets.items():
            Tx, Ty = Tx + P2*int(1e13), Ty + P2*int(1e13)
            A = (By*Tx - Bx*Ty) / (Ax*By-Ay*Bx)
            B = (Ax * Ty - Ay * Tx) / (Ax * By - Ay * Bx)
            if A.is_integer() and B.is_integer():
                res[P2] += 3 * int(A) + int(B)
    return res

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    