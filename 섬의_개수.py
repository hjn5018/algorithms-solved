directions = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0)]
# print(f"{directions = }")

from pprint import pprint
from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    # pprint(island)

    visited = []
    cnt_island = 0
    for i in range(w):
        for j in range(h):
            if (i, j) not in visited:
                visited.append((i, j))
                if island[j][i] == 1:
                    q = deque([(i, j)])
                    while q:
                        a, b = q.popleft()
                        for dx, dy in directions:
                            x, y = a + dx, b + dy
                            if 0 <= x < w and 0 <= y < h:
                                if (x, y) not in visited and island[y][x] == 1:
                                    q.append((x, y))
                                    visited.append((x, y))
                    cnt_island += 1
    print(cnt_island)
# https://www.acmicpc.net/problem/4963
