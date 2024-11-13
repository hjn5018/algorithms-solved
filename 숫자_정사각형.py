N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_ = min(N, M)
def solve(N:int, M:int, min_:int, board:list):
    while min_ != 1:
        for i in range(N-min_+1):
            for j in range(M-min_+1):
                if i+min_-1 < N and j+min_-1 < M:
                    if board[i][j] == board[i][j+min_-1] and board[i][j] == board[i+min_-1][j] and board[i][j] == board[i+min_-1][j+min_-1]:
                        return min_*min_
                else:
                    break
        min_ -= 1
    return 1

result = solve(N, M, min_, board)
print(result)
# https://www.acmicpc.net/problem/1051
