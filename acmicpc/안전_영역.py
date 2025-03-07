def get_count(N:int, arr2:list) -> int:
    '''
    bfs로 안전 영역을 완전 탐색한다.
    O(N^2)일 것으로 예상상
    '''
    from collections import deque

    count = 0
    visited = [[0] * N for _ in range(N)]
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    q = deque()
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and not arr2[i][j]:
                q.append((i, j))
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
                            if not visited[nx][ny] and not arr2[nx][ny]:
                                q.append((nx, ny))
                                visited[nx][ny] = True
                count += 1
    
    return count

def get_heights(N: int, arr1:list) -> list:
    min_h = float("inf")
    max_h = float("-inf")

    for i in range(N):
        for j in range(N):
            min_h = min(min_h, arr1[i][j])
            max_h = max(max_h, arr1[i][j])
    
    return [min_h, max_h]

def get_map(N:int, arr1:list, h:int) -> list:
    '''
    침수 지역은 1, 침수되지 않은 지역은 0인 2차원 배열을 반환한다.
    시간 복잡도는 O(N^2)
    '''

    result = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr1[i][j] <= h:
                result[i][j] = 1
    
    return result

def solve(N: int, arr1:list):
    '''
    강수량에 따라 각 안전 영역의 수를 구하고, 최대값을 출력한다.
    h의 범위는 1부터 100까지이고, N의 범위는 2부터 100까지이므로
    시간 복잡도는 O(h*N^2)인 O(100^3)으로 예상한다.
    '''
    min_h, max_h = get_heights(N, arr1)
    max_safe_area = 1
    
    for h in range(min_h, max_h + 1):
        arr2 = get_map(N, arr1, h)
        count_safe_area = get_count(N, arr2)
        max_safe_area = max(count_safe_area, max_safe_area)

    print(max_safe_area)
    return

# 입력 (2 <= N <= 100, 1 <= h <= 100)
N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]

solve(N, arr1)
# https://www.acmicpc.net/problem/2468
