N = int(input())
nums = [input() for _ in range(N)]

idx = 1
while True:
    new_nums = [num[-idx:] for num in nums]
    if len(nums) == len(set(new_nums)):
        break
    else:
        idx += 1
print(idx)
# https://www.acmicpc.net/problem/1235
