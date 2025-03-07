def solution(answers):
    answer = []
    supoja1 = [(i%5)+1 for i in range(len(answers))]
    supoja2 = [[1,3,4,5][(i//2%4)] if i%2 else 2 for i in range(len(answers))]
    supoja3 = [[3,3,1,1,2,2,4,4,5,5][(i%10)] for i in range(len(answers))]
    a,b,c = 0,0,0
    for i,v in enumerate(answers):
        if v == supoja1[i]:
            a += 1
        if v == supoja2[i]:
            b += 1
        if v == supoja3[i]:
            c += 1
    if max(a,b,c) == a and max(a,b,c) == b and max(a,b,c) == c:
        return [1,2,3]
    if max(a,b,c) == a and max(a,b,c) == b:
        return [1,2]
    if max(a,b,c) == b and max(a,b,c) == c:
        return [2,3]
    if max(a,b,c) == a and max(a,b,c) == c:
        return [1,3]
    if max(a,b,c) == a:
        return [1]
    if max(a,b,c) == b:
        return [2]
    if max(a,b,c) == c:
        return [3]
        
    return answer
  # https://school.programmers.co.kr/learn/courses/30/lessons/42840
