x1, y1, x2, y2, x3, y3 = map(int, input().split())
def distance(a:int, b:int, c:int, d:int) -> int:
    return ((a-c)**2 + (b-d)**2)**0.5

if x1-x2 == 0 and x1-x3 == 0:
    print(-1.0)
elif (y1-y3)*(x1-x2) == (y1-y2)*(x1-x3):
    print(-1.0)
else:
    max_ = max(distance(x1, y1, x2, y2), distance(x2, y2, x3, y3), distance(x3, y3, x1, y1))
    min_ = min(distance(x1, y1, x2, y2), distance(x2, y2, x3, y3), distance(x3, y3, x1, y1))
    mid_ = distance(x1, y1, x2, y2) + distance(x2, y2, x3, y3) + distance(x3, y3, x1, y1) - max_ - min_
    print(2*(max_ + mid_) - 2*(mid_ + min_))
# https://www.acmicpc.net/problem/1064
