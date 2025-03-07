def solution(numbers, hand):
    answer = ''
    key = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    L, R = '*', '#'
    L_position = (3,0)
    R_position = (3,2)
    num_position = (0,0)
    d = 0
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += "L"
            L = numbers[i]
        elif numbers[i] in [3, 6, 9]:
            answer += "R"
            R = numbers[i]
        elif numbers[i] in [2, 5, 8, 0]:
            for j in range(len(key)):
                for k in range(len(key[j])):
                    if L == key[j][k]:
                        L_position = (j,k)
                    if R == key[j][k]:
                        R_position = (j,k)
                    if numbers[i] == key[j][k]:
                        num_position = (j,k)
            x1, y1 = L_position
            x2, y2 = R_position
            x3, y3 = num_position
            if abs(x2-x3) + abs(y2-y3) < abs(x1-x3) + abs(y1-y3):
                answer += "R"
                R = numbers[i]
            elif abs(x2-x3) + abs(y2-y3) > abs(x1-x3) + abs(y1-y3):
                answer += "L"
                L = numbers[i]
            else:
                if hand == 'right':
                    answer += "R"
                    R = numbers[i]
                else:
                    answer += "L"
                    L = numbers[i]
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/67256
