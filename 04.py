from time import perf_counter
import numpy as np

def main():
    txt = np.array([list(row) for row in open("4.txt").read().strip().split()])

    p1 = sum(''.join(line).count("XMAS") + ''.join(line).count("SAMX") for line in np.vstack([txt, txt.T]))

    for _ in range(2):
        p1 += sum(''.join(np.diag(txt, i)).count("XMAS") + ''.join(np.diag(txt, i)).count("SAMX")
                  for i in range(-txt.shape[0] + 1, txt.shape[1]))
        txt = np.fliplr(txt)
        
    p2 = sum((txt[y-1, x-1] + txt[y, x] + txt[y+1, x+1] in "MAS SAM") and 
             (txt[y+1, x-1] + txt[y, x] + txt[y-1, x+1] in "MAS SAM")
             for y in range(1, txt.shape[0] - 1) for x in range(1, txt.shape[1] - 1))

    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")