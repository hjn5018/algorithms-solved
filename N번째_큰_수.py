import heapq

N = int(input())
heap = []

for _ in range(N):
    row = map(int, input().split())
    for num in row:
        heapq.heappush(heap, num)
        if len(heap) > N:
            heapq.heappop(heap)

print(heap[0])
# https://www.acmicpc.net/problem/2075
