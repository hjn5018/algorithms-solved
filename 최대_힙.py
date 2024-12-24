import sys, heapq
input = sys.stdin.readline

list_ = []

N = int(input())
for _ in range(N):
    input_ = int(input())
    if input_ == 0:
        if list_ == []:
            print(0)
        else:
            print(-heapq.heappop(list_))
    else:
        heapq.heappush(list_, -input_)

# https://www.acmicpc.net/problem/11279
