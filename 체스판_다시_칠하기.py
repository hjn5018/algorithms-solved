N, M = map(int, input().split())
board = [input() for _ in range(N)]

sample_line = ['W' if i % 2 == 0 else 'B' for i in range(8)]
sample = [sample_line if i % 2 == 0 else sample_line[::-1] for i in range(8)]

# 8x8 보드를 받으면 paint_count를 반환하는 함수
def paint_count(splited_board, sample=sample):
    w_count = 0
    b_count = 0
    # '잘라낸 8x8 보드를 'W' 또는 'B'를 시작점으로 하는 샘플과 비교하고,
    # 최소값을 반환한다.'
    for i in range(8):
        for j in range(8):
            if splited_board[0][0] == 'W':
                if splited_board[i][j] != sample[i][j]:
                    w_count += 1
                else:
                    b_count += 1
            else:
                if splited_board[i][j] == sample[i][j]:
                    w_count += 1
                else:
                    b_count += 1
    return min(w_count, b_count)

# board에서 (i, j)를 시작점으로 하는 8x8 보드를 잘라내어 반환하는 함수
def split_board(i, j):
    splited_board = [[0] * 8 for _ in range(8)]
    for x in range(i, i + 8):
        for y in range(j, j + 8):
            splited_board[x - i][y - j] = board[x][y]
    return splited_board

# 0에서 N - 8까지, 0에서 M - 8까지의 시작점 (i, j)를 얻는다.
def get_starting_coordinates(board):
    starting_coordinates = []
    for i in range(N - 8 + 1):
        for j in range(M - 8 + 1):
            starting_coordinates.append([i, j])
    return starting_coordinates

# 시작점으로 보드를 잘라낸다.
starting_coordinates = get_starting_coordinates(board)
splited_boards = []
for i, j in starting_coordinates:
    splited_board = split_board(i, j)
    splited_boards.append(splited_board)
    
# 잘라낸 보드로 paint_count를 구한다.
count_list = []
for splited_board in splited_boards:
    count_list.append(paint_count(splited_board))
print(min(count_list))
# 모든 시작점을 토대로 구한 paint_count 중 최소값을 출력한다.
# https://www.acmicpc.net/problem/1018
