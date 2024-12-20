from time import perf_counter

def main():
    p1, p2 = 0, 0
    
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")
    