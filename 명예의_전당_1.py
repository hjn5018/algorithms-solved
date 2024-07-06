def solution(k, score):
    answer = []
    for i in range(len(score)):
        sorted_score = sorted(score[:i+1], reverse=True)
        honor = sorted_score[:k]
        answer.append(honor[-1])
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/138477
