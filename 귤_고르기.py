def solution(k, tangerine):
    count_by_size = {}
    for i in tangerine:
        if i in count_by_size:
            count_by_size[i] += 1
        else:
            count_by_size[i] = 1
    count = list(count_by_size.values())
    count.sort()
    answer = 1
    sum = 0
    for i in range(len(count) - 1, -1, -1):
        sum += count[i]
        if sum >= k:
            return answer
        answer += 1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/138476
