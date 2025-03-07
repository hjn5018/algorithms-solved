N = int(input())
cards = list(map(int, input().split()))
cards_dict = {}
for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

M = int(input())
integers = list(map(int, input().split()))
for integer in integers:
    if integer in cards_dict:
        print(cards_dict[integer], end=' ')
    else:
        print(0, end=' ')
# https://www.acmicpc.net/problem/10816
