import sys
import heapq

input = sys.stdin.read
lines = input().splitlines()

N = int(lines[0])
heap = []

result = []
for i in range(1, N + 1):
    x = int(lines[i])
    if x == 0:
        if heap:
            result.append(heapq.heappop(heap)[1])  # 실제 값을 출력
        else:
            result.append(0)
    else:
        heapq.heappush(heap, (abs(x), x))  # (절댓값, 원래 값) 형태로 저장

print("\n".join(map(str, result)))

import sys

# class AbsMinHeap:
#     def __init__(self):
#         self.heap = []

#     def push(self, x):
#         """절댓값 기준으로 최소힙에 원소 추가"""
#         self.heap.append(x)
#         self._heapify_up(len(self.heap) - 1)

#     def pop(self):
#         """절댓값이 가장 작은 값 반환 및 제거"""
#         if not self.heap:
#             return 0  # 비어 있으면 0 반환

#         if len(self.heap) == 1:
#             return self.heap.pop()  # 원소가 하나일 경우 바로 반환

#         # 루트 원소를 반환하고 마지막 원소와 교체 후 힙 정렬
#         root = self.heap[0]
#         self.heap[0] = self.heap.pop()
#         self._heapify_down(0)
#         return root

#     def _heapify_up(self, index):
#         """삽입 후 위로 올려서 힙 속성 유지"""
#         while index > 0:
#             parent = (index - 1) // 2
#             if self._compare(self.heap[index], self.heap[parent]):
#                 self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
#                 index = parent
#             else:
#                 break

#     def _heapify_down(self, index):
#         """삭제 후 아래로 내려서 힙 속성 유지"""
#         size = len(self.heap)
#         while True:
#             left = 2 * index + 1
#             right = 2 * index + 2
#             smallest = index

#             if left < size and self._compare(self.heap[left], self.heap[smallest]):
#                 smallest = left
#             if right < size and self._compare(self.heap[right], self.heap[smallest]):
#                 smallest = right

#             if smallest != index:
#                 self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
#                 index = smallest
#             else:
#                 break

#     def _compare(self, a, b):
#         """절댓값이 작은 것이 우선, 같다면 원래 값이 작은 것이 우선"""
#         return abs(a) < abs(b) or (abs(a) == abs(b) and a < b)


# def main():
#     input = sys.stdin.read
#     lines = input().splitlines()
    
#     N = int(lines[0])
#     heap = AbsMinHeap()
#     result = []

#     for i in range(1, N + 1):
#         x = int(lines[i])
#         if x == 0:
#             result.append(str(heap.pop()))
#         else:
#             heap.push(x)

#     print("\n".join(result))


# if __name__ == "__main__":
#     main()

# https://www.acmicpc.net/problem/11286
