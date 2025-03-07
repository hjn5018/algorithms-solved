t = int(input())

def koong(n:int) -> int:
    if n < 2:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4]
        return dp[n]

for _ in range(t):
    n = int(input())
    result = koong(n)
    print(result)
# https://www.acmicpc.net/problem/9507
