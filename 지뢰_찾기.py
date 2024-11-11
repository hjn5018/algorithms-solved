n = int(input())
mine_board = [input() for _ in range(n)]
opened_board = [input() for _ in range(n)]
board = [['.']*n for _ in range(n)]

def mark_all_mines(mine_board:list, board:list):
    for i in range(n):
        for j in range(n):
            if mine_board[i][j] == '*':
                board[i][j] = '*'

directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
flag = False
for i in range(n):
    for j in range(n):
        if opened_board[i][j] == 'x':
            if mine_board[i][j] == '*':
                flag = True
            elif mine_board[i][j] == '.':
                count = 0
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                        if mine_board[nx][ny] == '*':
                            count += 1
                    board[i][j] = count

if flag:
    mark_all_mines(mine_board, board)

for i in range(n):
    print(''.join(map(str, board[i])))

# https://www.acmicpc.net/problem/4396
