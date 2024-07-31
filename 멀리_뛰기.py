def solution(n):
    memo = [1, 2]
    a, b = memo
    for _ in range(n-1):
        a, b = b, a + b
    return a % 1234567
# https://school.programmers.co.kr/learn/courses/30/lessons/12914
