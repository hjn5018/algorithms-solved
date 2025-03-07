import math

def solution(n, words):
    link = words[0][0]
    said = []
    for i in range(len(words)):
        if len(words[i]) < 2:
            return [((i + 1) % n) if ((i + 1) % n) else n, math.ceil((i + 1) / n)]
        if not words[i].startswith(link):
            return [((i + 1) % n) if ((i + 1) % n) else n, math.ceil((i + 1) / n)]
        if words[i] in said:
            return [((i + 1) % n) if ((i + 1) % n) else n, math.ceil((i + 1) / n)]
        link = words[i][-1]
        said.append(words[i])
    return [0, 0]
# https://school.programmers.co.kr/learn/courses/30/lessons/12981
