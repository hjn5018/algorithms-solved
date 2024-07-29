def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
            continue
            
        if stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    return 1
# https://school.programmers.co.kr/learn/courses/30/lessons/12973


94.2/100
from collections import deque

def solution(s):
    stack = []
    s_list = [i for i in s]
    s_deque = deque(s_list)
    while True:
        stack.append(s_deque[0])
        s_deque.popleft()
        if not s_deque and stack:
            return 0
        while True:
            if s_deque and stack:
                if stack[-1] == s_deque[0]:
                    stack.pop()
                    s_deque.popleft()
                else:
                    break
            else:
                break
        if not s_deque:
            return 1
# for문으로 해보다가 어려워서 while로 전환했다.
# while로 풀어도 힘들어서 deque를 썼다.
# deque를 써도 break, return 짜기 힘들어서 한계에 부딪혔다.
# 질문하기에서 stack을 쓴 풀이가 있어서 보았다.
# stack에 더불어 for문을 사용했는데, for문에서 continue를 주고 s[i]를 흘려보내는 유연함이 있었다.
# 나는 s[i]를 없애야한다는 강박이 들어서 떠올리기 어려운 유형이었다.
