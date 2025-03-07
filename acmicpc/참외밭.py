from collections import Counter

dc = int(input())

D = []
L = []
for _ in range(6):
    d, l = map(int, input().split())
    D.append(d)
    L.append(l)

large_rectangle = 1
Counter_D = Counter(D)
splited = set()
for d, i in Counter_D.items():
    if i == 1:
        large_rectangle *= L[D.index(d)]
    else:
        splited.add(d)

small_rectangle = 1
for i in range(1, len(D) - 1):
    if D[i - 1] in splited:
        if D[i + 1] in splited:
            small_rectangle *= L[i]

if D[1] in splited:
    if D[-1] in splited:
        small_rectangle *= L[0]

if D[-2] in splited:
    if D[0] in splited:
        small_rectangle *= L[-1]


farm = large_rectangle - small_rectangle
result = farm * dc
print(result)
# https://www.acmicpc.net/problem/2477
