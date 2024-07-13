from string import ascii_uppercase

def solution(keymap, targets):
    answer = []
    a = dict()
    for i in ascii_uppercase:
        a[i] = 0
    
    for i in a:
        temp = []
        for j in keymap:
            if i in j:
                temp.append(j.index(i)+1)
        if temp == []:
            a[i] = 0
        else:
            a[i] = min(temp)
    
    for i,v in enumerate(targets):
        numlist = []
        for j in v:
            if a[j] == 0:
                numlist.append(0)
                break
            else:
                numlist.append(a[j])
        if 0 in numlist:
            answer.append(-1)
        else:
            answer.append(sum(numlist))
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/160586#
