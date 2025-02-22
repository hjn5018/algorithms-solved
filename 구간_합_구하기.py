import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 누적 합 배열 초기화
S = [[0] * (N + 1) for _ in range(N + 1)]

# 누적 합 배열 만들기
for i in range(1, N + 1):
    for j in range(1, N + 1):
        S[i][j] = A[i-1][j-1] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]

# 쿼리 처리
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = S[x2][y2] - S[x1-1][y2] - S[x2][y1-1] + S[x1-1][y1-1]
    print(result)
# https://www.acmicpc.net/problem/11660
