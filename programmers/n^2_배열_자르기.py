def solution(n, left, right):
    answer = []
    a, b = divmod(left, n)
    c, d = divmod(right, n)
    # print(f'{a, b, c, d = }')
    while True:
        answer.append(max(a + 1, b + 1))
        b += 1
        if b == n:
            a += 1
            b = 0
        if a == c and b == d:
            answer.append(max(a + 1, b + 1))
            return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/87390
