def parse(x:int, y:int, N:int):
    global result
    start = arr[y][x]
    for i in range(N):
        for j in range(N):
            if arr[y + i][x + j] != start:
                result += '('
                parse(x, y, N//2)
                parse(x + N//2, y, N//2)
                parse(x, y + N//2, N//2)
                parse(x + N//2, y + N//2, N//2)
                result += ')'
                return
    result += str(start)

N = int(input())
arr = [list(input()) for _ in range(N)]
result = ""
parse(0, 0, N)

print(result)
# https://www.acmicpc.net/problem/1992
