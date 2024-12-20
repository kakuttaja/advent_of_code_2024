from time import perf_counter
from collections import defaultdict

def main():
    txt = open("5.txt").read().strip().split()

    rules = defaultdict(list)
    p1, p2 = 0, 0
    while True:
        if "|" not in txt[0]: break
        a, b = txt.pop(0).split("|")
        rules[a].append(b)
        
    pages = [page.split(',') for page in txt]
    check = lambda x, d: all(x.index(p) > x.index(num) for num in x for p in d[num] if p in x)
    reorder = lambda x, d: all(x.insert(j, x.pop(i)) or False 
               for i, num in enumerate(x[1:], 1) 
               for j in range(i) if x[j] in d[num])
    
    p1 = sum(int(page[len(page) // 2]) for page in pages if check(page, rules))
    for page in pages:
        if check(page, rules): continue
        while not reorder(page, rules):
            continue
        p2 += int(page[len(page) // 2])
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")