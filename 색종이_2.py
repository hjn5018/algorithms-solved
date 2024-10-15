N = int(input())
board = [[0]*100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for j in range(10):
        for i in range(10):
            if y+j <= 100 and x+i <= 100:
                board[y+j][x+i] = 1

circumference = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and j == 99:
            circumference += 1
        elif j > 0:
            if board[i][j-1] == 0 and board[i][j] == 1:
                circumference += 1
            elif board[i][j-1] == 1 and board[i][j] == 0:
                circumference += 1

for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and i == 99:
            circumference += 1
        elif i > 0:
            if board[i-1][j] == 0 and board[i][j] == 1:
                circumference += 1
            elif board[i-1][j] == 1 and board[i][j] == 0:
                circumference += 1
print(circumference)

# https://www.acmicpc.net/problem/2567
