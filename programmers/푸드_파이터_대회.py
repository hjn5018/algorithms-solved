def solution(food):
    answer = ''
    for i,v in enumerate(food[1:]):
        if v >= 2:
            for _ in range(v//2):
                answer += str(i+1)
    answer = answer + '0' + answer[::-1]
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/134240
