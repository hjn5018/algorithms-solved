def solution(n, m, section):
    answer = 0
    if m == 1:
        answer = len(section)
    else:
        while section:
            section = [i for i in section if i > section[0] + m - 1]
            answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/161989
