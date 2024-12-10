import sys

input = sys.stdin.readline

n = int(input())
list_ = []
nums = [i for i in range(n, 0 , -1)]
result = ""
count_plus = 0
for _ in range(n):
    input_ = int(input())
    
    if input_ > count_plus:
        for _ in range(input_ - count_plus):
            list_.append(nums.pop())
            result += "+"
            count_plus += 1

    if input_ == list_.pop():
        result += "-"
        continue
    else:
        result = "NO"
        break

if result == "NO":
    print(result)
else:
    result = list(result)
    for char in result:
        print(char)
# https://www.acmicpc.net/problem/1874
