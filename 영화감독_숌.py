N = int(input())

x = 666
count_666 = 0
while True:
    if '666' in str(x):
        count_666 += 1
    if count_666 == N:
        print(x)
        break
    else:
        x += 1
# https://www.acmicpc.net/problem/1436
