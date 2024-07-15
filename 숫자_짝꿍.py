from collections import Counter

def solution(X, Y):
    answer = ''
    common = Counter(X) & Counter(Y)
    if not common:
        return '-1'
    if common.keys() == Counter('0').keys():
        return '0'
    
    temp = []
    for i in common:
        for _ in range(common[i]):
            temp.append(i)
    temp.sort(reverse=True)
    temp = ''.join(temp)
    
    a = ['1', '0']
    a.sort(reverse=True)
    print(a)
    return temp
# https://school.programmers.co.kr/learn/courses/30/lessons/131128
