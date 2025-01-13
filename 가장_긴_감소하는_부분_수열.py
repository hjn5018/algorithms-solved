N = int(input())
A = list(map(int, input().split()))

# print(f"{N = }")
# print(f"{A = }")

dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
# print(f"{dp = }")

print(max(dp))

# https://www.acmicpc.net/problem/11722
