def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        numerator = stages.count(i)
        denominator = len([j for j in stages if j >= i])
        if denominator == 0:
            answer.append((i, 0))
        else:
            answer.append((i, numerator/denominator))
    answer.sort(key=lambda x:x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/42889
