from collections import deque

N = int(input())
nums = deque(map(int, input().split()))

result = [0] * N
for i in range(1, N + 1):
    a = nums.popleft()
    
    j = 0
    k = 0
    while k <= N -1:
        if j == a:
            while result[k] != 0:
                k += 1
            result[k] = i
            break
        elif result[k] == 0:
            j += 1
        elif result[k] != 0:
            pass
        k += 1
print(*result)
# https://www.acmicpc.net/problem/1138
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
N = int(input())
nums = list(map(int, input().split()))

result = [0] * N

for i in range(1, N + 1):  # 키 1부터 N까지 배치
    a = nums[i - 1]  # 현재 사람의 왼쪽에 있어야 하는 큰 사람 수
    j, k = 0, 0  # j: 현재까지 빈자리 개수, k: 배열 인덱스
    
    while k < N:
        if result[k] == 0:  # 빈자리일 때만 카운트
            if j == a:  # 빈 자리 개수가 a개가 되면 배치
                result[k] = i
                break
            j += 1  # 아직 원하는 개수만큼 지나지 않았으면 증가
        k += 1  # 다음 위치로 이동

print(*result)
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
N = int(input())  # 사람 수
heights = list(map(int, input().split()))  # 왼쪽에 있는 키 큰 사람 수 정보

result = [0] * N  # 최종 줄 서기 결과

for person in range(1, N + 1):  # 키가 작은 사람부터 배치 (1부터 N까지)
    count = heights[person - 1]  # 왼쪽에 있어야 하는 키 큰 사람 수
    idx = 0  # 위치 찾기

    # 빈 자리 찾으면서 count만큼 건너뛰기
    while count > 0 or result[idx] != 0:
        if result[idx] == 0:  # 빈 자리일 경우만 count 감소
            count -= 1
        idx += 1

    result[idx] = person  # 자리 배치

print(*result)  # 결과 출력
