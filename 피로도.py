from itertools import permutations

def solution(k, dungeons):
    # N개의 던전이 있다면, n!만큼 완전 탐색을 한다.
    
    # [a, b, c]에 대해서
    # [a, b, c], [b, a, c], ... ,[]
    # 가능한 모든 배치를 찾는다.
    all_cases = list(permutations(dungeons))
    
    # 각 배치에 대해서 조사한다.
    max_count = 0
    for case in all_cases:
        count = 0
        fatigue = k
        
        for i in range(len(dungeons)):
            if fatigue >= case[i][0]:
                fatigue -= case[i][1]
                count += 1
                
        if count > max_count:
            max_count = count
    return max_count
# https://school.programmers.co.kr/learn/courses/30/lessons/87946
