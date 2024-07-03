def solution(number):
    answer = 0
    result = []
    for i,v in enumerate(number):
        for j,w in enumerate(number[i+1:]):
            for k in number[i+j+2:]:
                if v + w + k == 0:
                    answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/131705
