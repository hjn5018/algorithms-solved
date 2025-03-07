def solution(priorities, location):
    l = len(priorities)
    tmp = [False if i != location else True for i in range(l)]
    
    answer = 0
    while priorities:
        process = priorities.pop(0)
        target = tmp.pop(0)
        
        if not priorities or process >= max(priorities):
            answer += 1
            if target:
                return answer
        else:
            priorities.append(process)
            tmp.append(target)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
