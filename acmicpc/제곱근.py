N = int(input())

def binary_search(N:int) -> int:
    start = 1
    end = N
    while True:
        mid = (start + end) // 2
        if mid ** 2 == N:
            return mid
        elif mid ** 2 < N:
            start = mid + 1
        elif mid ** 2 > N:
            end = mid - 1

print(binary_search(N))
# https://www.acmicpc.net/problem/13706
