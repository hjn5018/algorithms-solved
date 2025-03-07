def solution(ingredient):
    answer = 0
    temp = []
    for i in ingredient:
        temp.append(i)
        if temp[-4:] == [1,2,3,1]:
            temp.pop()
            temp.pop()
            temp.pop()
            temp.pop()
            answer += 1
    return answer
  # https://school.programmers.co.kr/learn/courses/30/lessons/133502
