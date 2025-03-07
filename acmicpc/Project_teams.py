n = int(input())
ws = list(map(int, input().split()))

ws.sort()
wg = [ws[i] +  ws[2*n-1-i] for i in range(n)]

print(min(wg))
# https://www.acmicpc.net/problem/20044
