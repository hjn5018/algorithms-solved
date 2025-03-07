N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

result = [[0]*K for _ in range(N)]
for i in range(N):
    for j in range(K):
        tmp = 0
        for k in range(M):
            tmp += A[i][k] * B[k][j]
        result[i][j] = tmp

for i in result:
    for j in i:
        print(j, end=' ')
    print()
# https://www.acmicpc.net/problem/2740
