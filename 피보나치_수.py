def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]

def solution(n):
    return fibonacci(n) % 1234567

# https://school.programmers.co.kr/learn/courses/30/lessons/12945
