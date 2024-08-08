import math

def solution(progresses, speeds):
    answer = []
    list_ = []
    for i, v in enumerate(progresses):
        list_.append(math.ceil((100 - v) / speeds[i]))
    standard = list_[0]
    count = 0
    for i in range(len(list_)):
        if list_[i] <= standard:
            count += 1
            if i == len(list_) - 1:
                answer.append(count)
                return answer
        else:
            answer.append(count)
            if i == len(list_) - 1:
                answer.append(1)
                return answer
            standard = list_[i]
            count = 1
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
