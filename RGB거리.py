import sys

# 입력 받기
n = int(sys.stdin.readline())  # 집 개수
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# DP 테이블 초기화 (첫 번째 집 비용 그대로 저장)
dp = [[0] * 3 for _ in range(n)]
dp[0] = cost[0]

# DP 수행
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]  # 빨강 선택
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]  # 초록 선택
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]  # 파랑 선택

# 최소 비용 출력
print(min(dp[n-1]))

# https://www.acmicpc.net/problem/1149
