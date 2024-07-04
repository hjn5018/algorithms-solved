def solution(s, n):
    answer = ''
    for i in s:
        if 65 <= ord(i) <= 90:
            if ord(i) + n <= 90:
                answer += chr(ord(i) + n)
            else:
                answer += chr(ord(i) - 26 + n)
        if 97 <= ord(i) <= 122:
            if ord(i) + n <= 122:
                answer += chr(ord(i) + n)
            else:
                answer += chr(ord(i) - 26 + n)
        if i == ' ':
            answer += i
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/12926
