N = int(input())

def is_good_word(string:str) -> bool:
    '''
    단어 위로 아치형 곡선을 그어
    A는 A끼리, B는 B끼리 쌍을 짓는다.
    
    좋은 단어의 조건
    1. 선끼리 교차하지 않는다.
    2. 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을 수 있다.
    예시)
    AABB
    ABBA
    ABBABB
    AA
    
    잘못된 예시)
    ABAB
    AAA
    AB
    '''
    if string.count('A') % 2 != 0:
        return False
    if string.count('B') % 2 != 0:
        return False
    
    stack = []
    for i in string:
        stack.append(i)
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                pass
    if stack:
        return False
    return True

count = 0
for _ in range(N):
    string = input()
    if is_good_word(string):
        count += 1
print(count)
# https://www.acmicpc.net/problem/3986
