N = int(input())

net_length = 0
dots = [list(map(int, input().split())) for _ in range(N)]

for i in range(len(dots)):
    min_ = 10**5
    for j in range(len(dots)):
        if i != j:
            if dots[i][1] == dots[j][1] and abs(dots[i][0] - dots[j][0]) < min_:
                min_ = abs(dots[i][0] - dots[j][0])
    net_length += min_

print(net_length)
# https://www.acmicpc.net/problem/15970
