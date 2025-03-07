def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            sum_ = 0
            for l in range(len(arr2)):
                sum_ += arr1[i][l] * arr2[l][j]
            answer[i][j] = sum_
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/12949
