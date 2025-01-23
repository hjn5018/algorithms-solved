import sys

# 무한대 설정
INF = sys.maxsize

# 도시의 수 입력
n = int(input().strip())

# 도시 간의 거리 행렬 입력
dist = []
for _ in range(n):
    dist.append(list(map(int, input().strip().split())))

# DP 테이블 초기화
dp = [[INF] * (1 << n) for _ in range(n)]
dp[0][1] = 0

# DP를 이용한 TSP 풀이
for mask in range(1 << n):
    for u in range(n):
        if not (mask & (1 << u)):
            continue
        for v in range(n):
            if mask & (1 << v) or dist[u][v] == 0:
                continue
            next_mask = mask | (1 << v)
            dp[v][next_mask] = min(dp[v][next_mask], dp[u][mask] + dist[u][v])

# 최종 최소 비용 계산
result = min(dp[i][(1 << n) - 1] + dist[i][0] for i in range(1, n) if dist[i][0] != 0)
print(result)

# https://www.acmicpc.net/problem/10971
