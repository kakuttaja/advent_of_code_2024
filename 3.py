import re

def main():
    x = open("3.txt").read().strip(); v = 1
    return (sum(int(a) * int(b) for a, b in re.findall(r"mul\((\d+),(\d+)\)", x)), 
            sum(int(a) * int(b) for t in re.findall(r"(don't\(\)|do\(\)|mul\(\d+,\d+\))", x)
                for m in [re.findall(r"(\d+),(\d+)", t)] 
                if (v := v and t != r"don't()" or t == r"do()") and m
                for a, b in m if t.startswith(r"m")))

if __name__ == '__main__':
    print(main())
