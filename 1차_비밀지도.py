def solution(n, arr1, arr2):
    answer = []
    bin1 = [bin(i)[2:] for i in arr1]
    bin2 = [bin(i)[2:] for i in arr2]
    for i,v in enumerate(bin1):
        if len(v) < n:
            bin1[i] = '0'*(n-len(v)) + bin1[i]
    for i,v in enumerate(bin2):
        if len(v) < n:
            bin2[i] = '0'*(n-len(v)) + bin2[i]
    for i in range(n):
        temp = ''
        for j in range(n):
            if bin1[i][j] == '1' or bin2[i][j] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/17681
