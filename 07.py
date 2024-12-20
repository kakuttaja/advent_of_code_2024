from time import perf_counter

def main():
    nums = []
    with open("7.txt") as f:
        for line in f.readlines():
            line = line.strip().replace(":", "")
            if not line: continue
            nums.append([int(i) for i in line.split()])
    p1, p2 = 0, 0
    done = set()
    def rec(nums, target, _p2=False):
        nonlocal p1, p2
        if nums[0] == target and len(nums) == 1:
            if _p2:
                p2 += target
                return 1
            if target not in done:
                p1 += target
                done.add(target)
            return True
        if len(nums) < 2 or nums[0] > target:
            return False
        if rec([nums[0] + nums[1]] + nums[2:], target, _p2) or rec([nums[0] * nums[1]] + nums[2:], target, _p2):
            return 1
        if _p2 and len(nums) > 1:
            return rec([int(str(nums[0]) + str(nums[1]))] + nums[2:], target, _p2)
        return 0
    for n in nums:
        rec(n[1:], n[0], _p2=True)
        rec(n[1:], n[0])
    return p1, p2

if __name__ == '__main__':
    start = perf_counter()
    print(*main())
    print(f"This took {round(perf_counter() - start, 2)}s")