import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# dp[i][j] = 위치 (i,j)에 도달할 수 있는 경로의 수
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1  # 시작 위치에는 1개의 경로로 도달 가능

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:  # 목적지에 도달했다면 루프 종료
            break
        
        if dp[i][j] == 0:  # 현재 위치에 도달할 수 없다면 스킵
            continue
        
        jump = board[i][j]
        if jump == 0:  # 현재 위치에서 이동할 수 없다면 스킵
            continue
        
        # 오른쪽으로 점프
        if j + jump < n:
            dp[i][j + jump] += dp[i][j]
        
        # 아래쪽으로 점프
        if i + jump < n:
            dp[i + jump][j] += dp[i][j]

print(dp[n-1][n-1])
# https://www.acmicpc.net/problem/1890
