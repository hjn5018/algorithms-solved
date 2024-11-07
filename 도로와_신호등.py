N, L = map(int, input().split())

signs = [list(map(int, input().split())) for _ in range(N)]

t, d, i = 0, 0, 0

while d < L:
    if i >= N:
        d += 1
    else:
        if d < signs[i][0]:
            d += 1
        elif d == signs[i][0]:
            if t % (signs[i][1] + signs[i][2]) < signs[i][1]:
                pass
            else:
                d += 1
                i += 1
    t += 1

print(t)
# https://www.acmicpc.net/problem/2980
