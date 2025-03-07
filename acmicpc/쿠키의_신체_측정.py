N = int(input())
board = [list(input()) for _ in range(N)]

def find_heart(board:list) -> tuple:
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*':
                heart = (i+1, j)
                return heart

heart = find_heart(board)
x, y = heart
left_arm = 0
for i in range(y):
    if board[x][i] == '*':
        left_arm += 1
        
right_arm = 0
for i in range(y+1, N):
    if board[x][i] == '*':
        right_arm += 1

body = 0
for i in range(N):
    if board[i][y] == '*':
        body += 1
body -= 2 # 머리와 심장의 길이를 제외한다.

end_of_body = (x+body, y)
left_leg = 0
for i in range(x+body+1, N):
    if board[i][y-1] == '*':
        left_leg += 1
        
right_leg = 0
for i in range(x+body+1, N):
    if board[i][y+1] == '*':
        right_leg += 1
        
print(x+1, y+1)
print(left_arm, right_arm, body, left_leg, right_leg)
# https://www.acmicpc.net/problem/20125
