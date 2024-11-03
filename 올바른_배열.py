N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

max_count = 0
for i in range(N):
    count = 1
    for j in range(1, 5):
        if nums[i]+j in nums:
            count += 1
    if count > max_count:
        max_count = count

if count != 5:
    print(5-max_count)
# https://www.acmicpc.net/problem/1337
