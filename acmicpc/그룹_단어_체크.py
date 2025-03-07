N = int(input())
count = 0
for _ in range(N):
    s = input()
    temp = ''
    flag = False
    for i, v in enumerate(s):
        if v not in temp:
            temp += v
        elif temp[-1] == v:
            pass
        else:
            flag = True
            break
    if i == len(s) - 1 and not flag:
        count += 1
print(count)
# https://www.acmicpc.net/problem/1316
