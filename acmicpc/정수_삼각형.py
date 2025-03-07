from copy import deepcopy

n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(len(nums)):
        arr[i][j] = nums[j]

dp = deepcopy(arr)

for i in range(1, n):
    for j in range(i+1):
        if j >= 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + arr[i][j]
        else:
            dp[i][j] = dp[i-1][j] + arr[i][j]

print(max(dp[n-1]))
# https://www.acmicpc.net/problem/1932
