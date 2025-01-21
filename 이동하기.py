from copy import deepcopy

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = deepcopy(maze)

for i in range(N):
    for j in range(M):
        if i == 0 and j != 0:
            dp[i][j] = dp[i][j-1] + dp[i][j]
        elif j == 0 and i != 0:
            dp[i][j] = dp[i-1][j] + dp[i][j]
        elif i != 0 and j != 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + dp[i][j]

print(dp[N-1][M-1])
# https://www.acmicpc.net/problem/11048
