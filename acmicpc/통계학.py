import sys
from collections import Counter

input = sys.stdin.readline
nums = [int(input()) for _ in range(int(input()))]
nums.sort()
l = len(nums)

# 산술 평균
sum_ = sum(nums)
if 0.5 <= sum_ / l - int(sum_ / l):
    print(sum_ // l + 1)
elif 0 <= sum_ / l - int(sum_ / l) <= 0.5:
    print(sum_ // l)
elif -0.5 < sum_ / l - int(sum_ / l) < 0:
    print(sum_ // l + 1)
else:
    print(sum_ // l)

# 중앙값
print(nums[l//2])

# 최빈값
C = Counter(nums)
items = C.items()
items = list(items)
items.sort(key=lambda x: (-x[1], x[0]))

if l > 1:
    if items[0][1] == items[1][1]:
        print(items[1][0])
    else:
        print(items[0][0])
else:
    print(nums[0])
# 범위
if l > 1:
    print(nums[-1] - nums[0])
else:
    print(0)
# https://www.acmicpc.net/problem/2108
