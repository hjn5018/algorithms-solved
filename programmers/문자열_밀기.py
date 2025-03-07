def solution(A, B):
    AA = A + A
    if B not in AA: # find all posible cases
        return -1
    
    count_push = 0
    if A == B:
        return 0
    
    for _ in range(len(A)):
        A = A[-1] + A[:-1]
        count_push += 1
        if A == B:
            return count_push
# https://school.programmers.co.kr/learn/courses/30/lessons/120921
