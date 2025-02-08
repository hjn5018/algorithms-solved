import sys

def max_profit(prices):
    max_price = 0
    profit = 0
    
    # 뒤에서부터 탐색
    for price in reversed(prices):
        if price > max_price:
            max_price = price
        else:
            profit += max_price - price
    
    return profit

# 입력 처리
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    prices = list(map(int, sys.stdin.readline().split()))
    print(max_profit(prices))

# https://www.acmicpc.net/problem/11501
