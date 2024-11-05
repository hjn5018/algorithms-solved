board = [[0]*30 for _ in range(30)]
for i in range(30):
    for j in range(i+1):
        if j == 0 or j == i:
            board[i][j] = 1
        else:
            board[i][j] = board[i-1][j] + board[i-1][j-1]

R, C, W = map(int, input().split())

result = 0
count = 1
for i in range(R-1, R+W-1):
    j = C-1
    for _ in range(count):
        result += board[i][j]
        j += 1
    count += 1

print(result)
# https://www.acmicpc.net/problem/15489
