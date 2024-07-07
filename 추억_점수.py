def solution(name, yearning, photo):
    answer = []
    for i in photo:
        score = 0
        for j in i:
            if j in name:
                score += yearning[name.index(j)]
        answer.append(score)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    yearning_dict = dict(zip(name, yearning))
    for i in photo:
        score = 0
        for j in i:
            if j in name:
                score += yearning_dict[j]
        answer.append(score)
    return answer

# 계속 index를 쓰는 것보다 한번 zip을 해두고 써먹는 게 낫지 않을까?
