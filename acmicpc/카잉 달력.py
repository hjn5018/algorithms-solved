import sys
import math

def find_year(M, N, x, y):
    lcm = M * N // math.gcd(M, N)  # M과 N의 최소공배수(LCM) 계산
    while x <= lcm:  # LCM을 초과하면 불가능하므로 종료
        if (x - 1) % N + 1 == y:  # x가 y에 해당하는 해인지 확인
            return x
        x += M  # x를 M씩 증가시켜 탐색
    return -1  # 찾을 수 없을 경우 -1 반환

# 입력 처리
T = int(sys.stdin.readline().strip())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    print(find_year(M, N, x, y))
# https://www.acmicpc.net/problem/6064
