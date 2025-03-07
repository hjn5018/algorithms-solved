N = int(input())
switches = list(map(int, input().split()))
M = int(input())
students = [map(int, input().split()) for _ in range(M)]

def male(v, switches=switches):
    for i in range(v-1, len(switches), v):
        if switches[i] == 0:
            switches[i] = 1
        else:
            switches[i] = 0

def female(v, switches=switches):
    v -= 1
    if switches[v] == 0:
        switches[v] = 1
    else:
        switches[v] = 0
    pointer1 = v - 1
    pointer2 = v + 1
    while pointer1 >= 0 and pointer2 <= len(switches)-1:
        if switches[pointer1] == switches[pointer2]:
            if switches[pointer1] == 0:
                switches[pointer1] = switches[pointer2] = 1
            else:
                switches[pointer1] = switches[pointer2] = 0
            pointer1 -= 1
            pointer2 += 1
        else:
            break


for i, v in students:
    if i == 1:
        male(v)
    elif i == 2:
        female(v)

for i in range(0, len(switches), 20):
    print(*switches[i:i+20])
# https://www.acmicpc.net/problem/1244
