from collections import deque

def func2(queue:deque):
    l = queue.popleft()
    queue.append(l)
    return queue

def func3(queue:deque):
    r = queue.pop()
    queue.appendleft(r)
    return queue

N, M = map(int, input().split())
positions = list(map(int, input().split()))

queue = deque(range(1, N+1))
targets = [queue[pos-1] for pos in positions]

count = 0
for i in range(len(targets)):
    while targets[i] != queue[0]:
        length = len(queue) - 1
        left = queue.index(targets[i])
        right = length - left
        if left <= right:
            queue = func2(queue)
        elif left > right:
            queue = func3(queue)
        # elif left == right:
        #     left = queue.index(targets[i+1])
        #     right = length - left
        #     if left < right:
        #         queue = func2(queue)
        #     elif left > right:
        #         queue = func3(queue)
        count += 1
    queue.popleft()

print(count)

# ---

from collections import deque

# 입력 처리
N, M = map(int, input().split())
positions = list(map(int, input().split()))

# 초기 큐 구성
queue = deque(range(1, N + 1))

count = 0  # 총 이동 횟수
for target in positions:
    # 타겟 원소의 위치 계산
    target_index = queue.index(target)
    left = target_index  # 왼쪽 이동 거리
    right = len(queue) - target_index  # 오른쪽 이동 거리

    # 최소 이동 방향으로 회전
    if left <= right:
        queue.rotate(-left)  # 왼쪽으로 회전
        count += left
    else:
        queue.rotate(right)  # 오른쪽으로 회전
        count += right

    # 현재 타겟 제거
    queue.popleft()

print(count)

# ---

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

dq = deque(i for i in range(1, N+1))
elements = list(map(int, input().split()))

answer = 0
for e in elements:
    count = 0
    v = dq.popleft()
    while v != e:
        dq.append(v)
        v = dq.popleft()
        count += 1
    
    answer += count if count < len(dq) + 1 - count else len(dq) + 1 - count
    
print(answer)

# https://www.acmicpc.net/problem/1021
