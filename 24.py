from time import perf_counter
import re

def simulate(wires, gates):
    wires = dict(wires)
    gates = dict(gates)
    OPS = {"XOR": lambda a, b: a ^ b,
           "OR": lambda a, b: a | b,
           "AND": lambda a, b: a & b}
    new = True
    done = set()
    while new:
        new = False
        for (a, b, op), c in gates.items():
            if (a, b, c) in done: continue
            if a in wires and b in wires:
                done.add((a, b, c))
                wires[c] = OPS[op](wires[a], wires[b])
                new = True
    return tuple(wires.items())

def compare_result(wires):
    x, y = [], []
    for k in sorted(wires.keys(), reverse=True):
        if k[0] == "x":
            x.append(str(wires[k]))
        if k[0] == "y":
            y.append(str(wires[k]))
    res = ''
    c = 0
    for i in range(len(x) - 1, -1, -1):
        r = c
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        res = ('1' if r % 2 == 1 else '0') + res
        c = 0 if r < 2 else 1
    if c != 0:
        res = '1' + res
    z = res
    faulty = set()
    n = ""
    for i, k in enumerate(sorted(wires.keys(), reverse=True)):
        if k[0] == "z":
            n += str(wires[k])
            if z[i] != n[-1]:
                faulty.add(k)
    return z, n, faulty


def main():
    from collections import Counter
    wires = {}
    txt = open("24.txt").read().strip().replace('\n', ' ')
    wirepaths = {}
    for wire, state in re.findall("(\w\w\w): (\d+)", txt):
        wires[wire] = int(state)
    r = re.findall("(\w{3}) (\w{2,3}) (\w{3}) \-\> (\w+)", txt)
    gates_init = {(a, b, op): c for a, op, b, c in r}
    wires = dict(simulate(tuple(wires.items()), tuple(gates_init.items())))
    exp = []
    opcount = Counter()
    opcolor = {
        "XOR": "orange",
        "OR": "lightblue",
        "AND": "purple"
    }
    # The power of GraphViz.. Yay. Like last year.
    # print("""digraph Circuit {
    # rankdir=LR;
    # node [shape=box, style=rounded];
    # gwh[style=filled, color=red]
    # jct[style=filled, color=red]
    # rcb[style=filled, color=red]
    # wbw[style=filled, color=red]
    # wgb[style=filled, color=red]
    # z09[style=filled, color=red]
    # z21[style=filled, color=red]
    # z39[style=filled, color=red]""")
    # for (a, op, b, c) in r:
    #     wirepaths[a] = c
    #     wirepaths[b] = c
    #     e1 = f"{a} -> {op}{opcount[op]} -> {c}"
    #     e2 = f"{b} -> {op}{opcount[op]} -> {c}"
    #     print(e1)
    #     print(e2)
    #     print(f"{op}{opcount[op]}[style=filled, color={opcolor[op]}]")
    #     exp.append(e1)
    #     exp.append(e2)
    #     opcount[op] += 1
    # print('->'.join(f"z{str(i).zfill(2)}" for i in range(46)))
    # print('->'.join(f"x{str(i).zfill(2)}" for i in range(45)))
    # print("}")
    z, n, _ = compare_result(wires)
    p1 = int(n, base=2)
    return p1, "gwh,jct,rcb,wbw,wgb,z09,z21,z39"

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")