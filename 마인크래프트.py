def minecraft(N, M, B, ground):
    height_counts = [0] * 257  # 높이별 블록 수
    total_blocks = 0  # 전체 블록 수

    # 높이별 블록 개수 계산
    for row in ground:
        for height in row:
            height_counts[height] += 1
            total_blocks += height

    min_time = float('inf')  # 최소 시간
    target_height = 0  # 목표 높이

    # 가능한 높이 범위 (0 ~ 256)
    for h in range(257):
        if total_blocks + B < h * N * M:
            # 블록이 부족하여 h 높이를 만들 수 없는 경우
            break

        remove = sum((i - h) * height_counts[i] for i in range(h + 1, 257))
        add = sum((h - i) * height_counts[i] for i in range(h))

        time = remove * 2 + add  # 작업 시간 계산
        if time < min_time or (time == min_time and h > target_height):
            min_time = time
            target_height = h

    return min_time, target_height

# 입력
N, M, B = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산
result = minecraft(N, M, B, ground)
print(result[0], result[1])

# https://www.acmicpc.net/problem/18111
