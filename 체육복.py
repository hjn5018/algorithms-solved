def solution(n, lost, reserve):
    check = [0] * n
    for i in lost:
        check[i-1] -= 1
    for i in reserve:
        check[i-1] += 1
    if check[0] == -1 and check[1] == 1:
        check[0], check[1] = 0, 0
    if check[-1] == -1 and check[-2] == 1:
        check[-1], check[-2] = 0, 0
    for i in range(1, len(check)-1):
        if check[i] == -1:
            if check[i-1] == 1:
                check[i], check[i-1] = 0, 0
            elif check[i+1] == 1:
                check[i], check[i+1] = 0, 0
    return sum([1 for i in check if i >= 0])
  # https://school.programmers.co.kr/learn/courses/30/lessons/42862#
