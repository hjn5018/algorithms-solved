N = int(input())

members = [input().split() for _ in range(N)]

temp = [[int(age), i, name] for i, [age, name] in enumerate(members)]
temp.sort()
for age, i, name in temp:
    print(age, name)
# https://www.acmicpc.net/problem/10814
