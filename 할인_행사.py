def solution(want, number, discount):
    answer = 0
    list_1 = []
    for i in range(len(number)):
        for j in range(number[i]):
            list_1.append(want[i])
    list_1.sort()
    for i in range(len(discount) - 9):
        list_ = []
        for j in discount[i:i+10]:
            list_.append(j)
        list_.sort()
        if list_1 == list_:
            answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/131127
