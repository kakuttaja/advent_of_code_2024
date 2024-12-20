from time import perf_counter

def main():
    txt = open("9.txt").read().strip()
    p1, p2 = 0, 0
    diskmap = []
    k = 0
    for i in range(len(txt)):
        if i == 0:
            diskmap += [str(k)] * int(txt[i])
            k += 1
        elif i % 2 == 0:
            diskmap += [str(k)] * int(txt[i])
            k += 1
        else:
            diskmap += ["."] * int(txt[i])
    diskmap2 = [i for i in diskmap]
    end = len(diskmap2)
    for i in range(len(diskmap) - 1, -1, -1):
        print(f"{end - i}/{end}                        ", end="\r")
        if "." in diskmap and diskmap.index(".") < i:
            diskmap[diskmap.index(".")] = diskmap[i]
            diskmap[i] = "."
    i = len(diskmap2) - 1
    # print(''.join(diskmap2))
    while i >= 0:
        print(f"{end - i}/{end}                        ", end="\r")
        n = diskmap2[i]
        j = i
        idx = -1

        if n == ".":
            i -= 1
            continue

        while j >= 0:
            if diskmap2[j - 1] != n:
                break
            j -= 1

        free = 0
        for k in range(diskmap2.index("."), j):
            if diskmap2[k] == ".":
                free += 1
            else:
                free = 0
            if free == (i - j + 1):
                idx = k - free + 1
                break

        if idx < j and idx != -1:
            diskmap2 = (diskmap2[:idx] + 
                        diskmap2[j:i + 1] + 
                        diskmap2[idx + (i - j + 1):j] + 
                        ["."] * (i - j + 1) + 
                        diskmap2[i + 1:])
        # print(''.join(diskmap2))
        i = j - 1
    for i in range(len(diskmap)):
        if diskmap[i] != ".":
            p1 += int(diskmap[i]) * i
        if diskmap2[i] != ".":
            p2 += int(diskmap2[i]) * i
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    