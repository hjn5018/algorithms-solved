def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk == []:
            stk += [arr[i]]
        else:
            if stk[-1] == arr[i]:
                stk = stk[:-1]
            else:
                stk += [arr[i]]
    if stk == []:
        return [-1]
    else:
        return stk
# https://school.programmers.co.kr/learn/courses/30/lessons/181859
