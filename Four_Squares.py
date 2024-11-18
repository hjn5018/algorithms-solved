import math

def is_square(n):
    """n이 제곱수인지 확인"""
    return int(math.sqrt(n)) ** 2 == n

def min_square_sum_optimized(n):
    # 1. 하나의 제곱수로 표현 가능한 경우
    if is_square(n):
        return 1
    
    # 2. 두 개의 제곱수로 표현 가능한지 확인
    for i in range(1, int(math.sqrt(n)) + 1):
        if is_square(n - i * i):
            return 2
    
    # 3. 네 제곱수 정리: n이 4^a(8b + 7) 형태인지 확인
    temp = n
    while temp % 4 == 0:
        temp //= 4
    if temp % 8 == 7:
        return 4
    
    # 4. 세 개의 제곱수로 표현 가능 (나머지 경우)
    return 3

# 입력 처리 및 결과 출력
n = int(input().strip())
print(min_square_sum_optimized(n))

# https://www.acmicpc.net/problem/17626
