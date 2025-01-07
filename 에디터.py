from collections import deque
import sys
input = sys.stdin.readline

# 초기 문자열과 명령 입력
String = deque(input().strip())  # 초기 문자열을 deque로 변환
M = int(input())  # 명령의 개수

left = deque(String)  # 커서 왼쪽 문자열
right = deque()  # 커서 오른쪽 문자열

for _ in range(M):
    command = input().strip()
    if command == 'L':
        if left:  # 왼쪽에 문자가 있다면
            right.appendleft(left.pop())  # 왼쪽에서 오른쪽으로 이동
    elif command == 'D':
        if right:  # 오른쪽에 문자가 있다면
            left.append(right.popleft())  # 오른쪽에서 왼쪽으로 이동
    elif command == 'B':
        if left:  # 왼쪽에 문자가 있다면
            left.pop()  # 왼쪽에서 삭제
    elif command.startswith('P'):  # 'P x' 명령 처리
        _, char = command.split()
        left.append(char)  # 왼쪽에 문자 추가

# 결과 출력: 왼쪽 + 오른쪽 문자열
print(''.join(left) + ''.join(right))

# https://www.acmicpc.net/problem/1406
