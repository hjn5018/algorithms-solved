def solution(arr):
    x = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i] % 2 == 0:
            if arr[i] == 100:
                x[i] = 3
            else:
                x[i] = 2
        if arr[i] < 50 and arr[i] % 2 == 1:
            if arr[i] == 1:
                x[i] = 5
            if arr[i] >= 25:
                x[i] = 1
            if 25 > arr[i] >= 12:
                x[i] = 2
            if 12 > arr[i] >= 6:
                x[i] = 3
            if 6 > arr[i] >= 3:
                x[i] = 4
        else:
            x[i] = 0
                
    return max(x)
# https://school.programmers.co.kr/learn/courses/30/lessons/181881
