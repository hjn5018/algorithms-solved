def solution(l, r):
    answer = []
    numlist = [i for i in range(l, r+1)]
    for i in numlist:
        if '1' not in str(i) and '2' not in str(i) and '3' not in str(i) and '4' not in str(i) and '6' not in str(i) and '7' not in str(i) and '8' not in str(i) and '9' not in str(i):
            answer.append(i)
    if answer == []:
        answer = [-1]
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/181921
