import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
else:
    nums = [int(input()) for _ in range(n)]
    nums.sort()

    def round_off(n: float) -> int:
        if n - int(n) >= 0.5:
            return int(n) + 1
        return int(n)

    cut = round_off(n*0.15)
    nums = nums[cut:len(nums)-cut]

    print(round_off(sum(nums)/len(nums)))
# https://www.acmicpc.net/problem/18110
