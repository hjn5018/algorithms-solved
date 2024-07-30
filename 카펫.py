def solution(brown, yellow):
    answer = []
    x = ((4 + brown)**2 - 16 * (brown + yellow))**1/2
    w = (4 + brown + ((4 + brown)**2 - 16 * (brown + yellow))**(1/2)) / 4
    h = ((brown + 4) / 2) - w
    return [w, h]
https://school.programmers.co.kr/learn/courses/30/lessons/42842
