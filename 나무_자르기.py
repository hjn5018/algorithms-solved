N, M = map(int, input().split())
trees = list(map(int, input().split()))

def get_cut_length(height):
    """height 높이로 자를 때 얻는 나무 길이 계산"""
    return sum(max(0, tree - height) for tree in trees)

# 이진 탐색 초기화
low, high = 0, max(trees)
result = 0

while low <= high:
    mid = (low + high) // 2  # 현재 중간 높이
    cut_length = get_cut_length(mid)  # 잘린 나무 길이 계산

    if cut_length >= M:  # 필요한 나무 길이를 만족하는 경우
        result = mid  # 현재 높이를 결과로 기록
        low = mid + 1  # 더 높은 높이를 시도
    else:  # 나무 길이가 부족한 경우
        high = mid - 1  # 더 낮은 높이를 시도

print(result)
# https://www.acmicpc.net/submit/2805/87645944
