N = int(input())
nums = list(map(int, input().split()))
sum_ = sum(nums)

result = 0
for i in range(N):
    sum_ -= nums[i]
    result += nums[i] * sum_

print(result)
# https://www.acmicpc.net/problem/13900
