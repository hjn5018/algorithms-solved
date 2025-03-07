def solution(n):            
    memo = []
    for i in range(1, n+1):
        while True:
            if '3' in str(i) or not i % 3 or i in memo:
                i += 1
            else:
                memo.append(i)
                break
    return memo.pop()    
#     문제 분석
#     3 -> 4
#     4 -> 5
#     7 -> 9 -> 10
#     n -> n` -> n`` -> n```
    
#     9 -> 12 -> 13 -> 14
#     10 -> 11 -> 12 -> 14 -> 15 -> 16
#     '3' not in str(n) and n % 3 and m not in memo
# https://school.programmers.co.kr/learn/courses/30/lessons/120871
