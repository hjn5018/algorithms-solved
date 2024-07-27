def solution(n):
    a = n//2 + 1
    idx = 1
    answer = 0
    while idx < a:
        sum = 0
        for i in range(idx, a + 1):
            sum += i
            if sum == n:
                answer += 1
                idx += 1
                break
            elif sum > n:
                idx += 1
                break
    return answer + 1

# https://school.programmers.co.kr/learn/courses/30/lessons/12924
