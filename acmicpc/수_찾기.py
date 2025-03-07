import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))
M = int(input())
X_list = list(map(int, input().split()))

for i in X_list:
    print(1) if i in A else print(0)
# https://www.acmicpc.net/problem/1920
