def mod_pow(a, b, c):
    if b == 0:
        return 1  # A^0 = 1
    half = mod_pow(a, b // 2, c)
    result = (half * half) % c
    if b % 2 == 1:
        result = (result * a) % c
    return result

# 입력 받기
A, B, C = map(int, input().split())

# 결과 출력
print(mod_pow(A, B, C))

# https://www.acmicpc.net/problem/1629
