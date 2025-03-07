MOD = 10007

def binomial_coefficient(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1  # nC0 = 1
        for j in range(1, min(i, k) + 1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % MOD

    return dp[n][k]

# 입력 받기
n, k = map(int, input().split())
print(binomial_coefficient(n, k))
# https://www.acmicpc.net/problem/11051
