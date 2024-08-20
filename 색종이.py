N = int(input())
board = [[0]*100 for _ in range(100)]
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            if board[i][j] == 1:
                continue
            board[i][j] = 1
            count += 1
print(f"{count = }")
# https://www.acmicpc.net/problem/2563
