def solution(board, h, w):
    n = len(board)
    count = 0
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n:
            if board[h_check][w_check] == board[h][w]:
                count += 1
    return count
# https://school.programmers.co.kr/learn/courses/30/lessons/250125
