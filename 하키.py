W, H, X, Y, P = map(int, input().split())

count = 0
for _ in range(P):
    x, y = map(int, input().split())
    # 1. 직사각형 안에 존재하는지 확인한다.
    if X <= x <= X+W and Y <= y <= Y+H:
        count += 1
    # 2. 왼쪽 원 안에 존재하는지 확인한다.
    elif (x-X)**2 + (y-(Y+H/2))**2 <= (H/2)**2:
        count += 1
    # 3. 오른쪽 원 안에 존재하는지 확인한다
    elif (x-(X+W))**2 + (y-(Y+H/2))**2 <= (H/2)**2:
        count += 1
print(count)
# https://www.acmicpc.net/problem/1358
