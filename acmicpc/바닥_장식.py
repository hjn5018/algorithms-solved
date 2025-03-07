N, M = map(int, input().split())
floor = [input() for _ in range(N)]

count = 0
for i in range(N):
    for j in range(M):
        if j == 0 and floor[i][j] == '-':
            count += 1
        elif i == 0 and floor[i][j] == '|':
            count += 1
        elif floor[i][j] == '-' and floor[i][j-1] == '-':
            pass
        elif floor[i][j] == '|' and floor[i-1][j] == '|':
            pass
        else:
            count += 1
print(count)
# https://www.acmicpc.net/problem/1388
