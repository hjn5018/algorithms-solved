N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort(reverse=True)

tmp = [-i for i in range(N)]

result = [nums[i] + tmp[i] if nums[i] + tmp[i] > 0 else 0 for i in range(N)]
print(sum(result))
# https://www.acmicpc.net/problem/1758
