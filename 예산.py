def find_budget_cut(requests, M, max_):
    low, high = 0, max_
    result = 0

    while low <= high:
        middle = (low + high) // 2

        # 현재 상한액으로 배분한 예산의 총합 계산
        allocated = sum(min(req, middle) for req in requests)

        if allocated <= M:
            # 예산 합계가 허용 범위 안에 있다면, 상한액을 올려본다
            result = middle
            low = middle + 1
        else:
            # 예산 합계가 초과되면, 상한액을 낮춘다
            high = middle - 1

    return result


# 입력 처리
N = int(input())
requests = list(map(int, input().split()))
M = int(input())

if sum(requests) <= M:
    # 요청한 예산의 총합이 허용 예산 이하라면 최대 요청값을 출력
    print(max(requests))
else:
    # 이분 탐색으로 상한액을 계산
    budget_cut = find_budget_cut(requests, M, max(requests))
    print(budget_cut)

# https://www.acmicpc.net/problem/2512
