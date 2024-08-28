x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

if x1 == x2:
    print(x3, end=' ')
elif x2 == x3:
    print(x1, end=' ')
else:
    print(x2, end=' ')


if y1 == y2:
    print(y3, end='')
elif y2 == y3:
    print(y1, end='')
else:
    print(y2, end='')
    
# x1, x2, x3 중 어느 두 수와도 같지 않은 수를 찾는다.
# y1, y2, y3 중 어느 두 수와도 같지 않은 수를 찾는다.
# 찾은 두 수를 합한 (x, y)가 네 번째 점의 좌표이다.

# https://www.acmicpc.net/problem/3009
