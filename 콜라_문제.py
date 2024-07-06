def solution(a, b, n):
    answer = 0
    while n >= a:
        r = n % a
        answer += (n // a) * b
        n = (n // a) * b + r
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/132267
