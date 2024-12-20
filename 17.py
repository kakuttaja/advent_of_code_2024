from time import perf_counter
import re

def run(p, a):
    ip, b, c = 0, 0, 0
    res = []
    C = [0, 1, 2, 3, a, b, c]
    while ip < len(p) - 1:
        op = p[ip]
        operand = p[ip + 1]
        if op not in (1, 3):
            operand = C[p[ip + 1]]
        match op:
            case 0: C[4] = int(C[4] / (2 ** operand))
            case 1: C[5] = C[5] ^ operand
            case 2: C[5] = operand % 8
            case 3: ip = operand if not C[4] == 0 else ip + 2; continue
            case 4: C[5] = C[5] ^ C[6]
            case 5: res.append(operand % 8)
            case 6: C[5] = int(C[4] / (2 ** operand))
            case 7: C[6] = int(C[4] / (2 ** operand))
        ip += 2
    return res

def rec(a, d, p):
    if d == len(p):
        return a
    for i in range(8):
        r = run(p, a*8 + i)
        if r[0] == p[-(d+1)]:
            res = rec(a * 8 + i, d + 1, p)
            if res:
                return res

def main():
    a, _, _, *p = [int(n) for n in re.findall("(\d+)", open("17.txt").read())]
    return ','.join(str(i) for i in run(p, a)), rec(0, 0, p)

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    