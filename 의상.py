def solution(clothes):
    answer = 1
    dict_ = {}
    for i in clothes:
        if i[1] in dict_:
            dict_[i[1]] += [i[0]]
        else:
            dict_[i[1]] = [i[0]]
    for i in dict_:
        answer *= (len(dict_[i]) + 1)
    return answer - 1
# https://school.programmers.co.kr/learn/courses/30/lessons/42578
