def solution(s):
    for j in range(len(s)):
        stack = ''
        count = 0
        gauge = 0
        for i in s:
            stack += i
            gauge += 1
            if '[]' in stack or '()' in stack or '{}' in stack:
                stack = stack[:-2]
                gauge -= 2
                if gauge == 0:
                    count += 1
        if gauge == 0:
            return count
        s = s[1:] + s[0]
    return 0
# https://school.programmers.co.kr/learn/courses/30/lessons/76502
