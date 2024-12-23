from time import perf_counter
from functools import lru_cache
import re

KEYS = {
     "7": 0+0j, "8": 1+0j, "9": 2+0j,
     "4": 0+1j, "5": 1+1j, "6": 2+1j,
     "1": 0+2j, "2": 1+2j, "3": 2+2j, 
     " ": 0+3j, "0": 1+3j, 'A': 2+3j,
}
DIRS = {
     " ": 0+0j, "^": 1+0j, 'A': 2+0j,
     "<": 0+1j, "v": 1+1j, ">": 2+1j,
}

@lru_cache(None)
def rec(s, e):
    pad = DIRS
    if s in KEYS and e in KEYS: pad = KEYS

    move = pad[e] - pad[s]
    x = "<"*-int(move.real) if move.real < 0 else ">"*int(move.real)
    y = "^"*-int(move.imag) if move.imag < 0 else "v"*int(move.imag)

    # In some situations vertical movements
    # HAVE to be prioritized over horizontal ones.
    # But only specific ones.
    # I don't know why.
    
    if s+e in ("^>" ,"^<" ,"vA" ,"A<" ,"5A" ,"2A" ,"8A" ,"A5" ,"A2" ,"A8" ,"19" ,"A4" ,"48"):
        return y+x+"A"
    return x+y+"A"

@lru_cache(None)
def solver(s, d):
    r = 0
    if d == 0: return len(s)
    for i, c in enumerate(s):
        r += solver(rec(s[i-1], c), d - 1)
    return r

def main():
    nums = re.findall("(\d+)", open("21.txt").read())
    return (sum([int(num) * solver(num + "A", d=3) for num in nums]), 
            sum([int(num) * solver(num + "A", d=26) for num in nums]))

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    