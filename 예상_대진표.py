def solution(n,a,b):
    i = 1
    while True:
        if (a - 1) // 2**i == (b - 1) // 2**i:
            return i
        i += 1
# https://school.programmers.co.kr/learn/courses/30/lessons/12985#
