def solution(n):
    result = 0
    for i in range(2, n+1):
        count = 0
        for j in range(1, int(i**0.5)+1):
            if count > 1:
                break
            if i % j == 0:                
                count += 1
        if count == 1:
            result += 1
    return result
# https://school.programmers.co.kr/learn/courses/30/lessons/12921
