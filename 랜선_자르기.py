K, N = map(int, input().split())
cords = [int(input()) for _ in range(K)]
cords.sort()

def cut(l: int, cords: list, count=0) -> int:
    new_cords = []
    for cord in cords:
        if cord >= l:
            new_cords.append(cord - l)
            count += 1
    if new_cords and new_cords != [0]:
        return cut(l, new_cords, count)
    else:
        return count
    

mid = (cords[0] + cords[-1]) // 2
left, right = 0, cords[-1]

while left <= right:
    if cut(mid, cords) >= N:
        left = mid + 1
    else:
        right = mid - 1
    mid = (left + right) // 2

print(mid)
# https://www.acmicpc.net/problem/1654
