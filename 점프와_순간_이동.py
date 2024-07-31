def solution(n):
    ans = 0
    while True:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            ans += 1
        if n == 0:
            return ans
# https://school.programmers.co.kr/learn/courses/30/lessons/12980
