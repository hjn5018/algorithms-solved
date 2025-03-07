def solution(s):
    answer = 0
    start = s[0]
    x, y = 0, 0
    for i in range(len(s)):
        if start == s[i]:
            x += 1
        else:
            y += 1
        if i+1 >= len(s):
            answer += 1
        elif x == y:
            start = s[i+1]
            answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/140108
