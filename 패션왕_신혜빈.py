for _ in range(int(input())):
    n = int(input())
    clothes = [input().split() for _ in range(n)]
    
    # 의상 종류별로 개수를 저장
    category_count = {}
    for _, category in clothes:
        category_count[category] = category_count.get(category, 0) + 1
    
    # 각 의상 종류별 경우의 수를 곱함
    result = 1
    for count in category_count.values():
        result *= (count + 1)
    
    # 알몸인 경우(모두 선택하지 않는 경우) 제외
    print(result - 1)

# https://www.acmicpc.net/problem/9375
