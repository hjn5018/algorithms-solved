brackets = input()

def count_cut_iron_bars(s: str) -> int:
    stack = []
    count = 0

    for i in range(len(s)):
        if s[i] == '(':
            stack.append('(')
        else:  # s[i] == ')'
            stack.pop()
            if s[i - 1] == '(':
                # 레이저인 경우
                count += len(stack)
            else:
                # 쇠막대기의 끝인 경우
                count += 1

    return count

# 테스트
print(count_cut_iron_bars(brackets))  # 출력: 17

# https://www.acmicpc.net/problem/10799
