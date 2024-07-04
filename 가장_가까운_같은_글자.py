def solution(s):
    answer = []
    for i,v in enumerate(s):
        distance = 0
        for j,w in enumerate(s[:i]):
            if w == v:
                distance = len(s[:i])-j
        if distance != 0:
            answer.append(distance)
        else:
            answer.append(-1)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/142086
