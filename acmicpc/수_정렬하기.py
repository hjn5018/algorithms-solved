import sys

N = int(sys.stdin.readline())

count = [0] * 10001

# 정렬할 리스트(numbers)를 순회하며
# 각 값(number)을 count[number] += 1로 기록한다.
for _ in range(N):
    number = int(sys.stdin.readline())
    count[number] += 1

# 정렬 결과를 나타내는 리스트(result)를 생성한다.
result = []

# 계수 리스트(count)를 순회하며
# 기록한 수(counted)만큼 반복하여 정렬할 값(number)를 result에 담는다.
for i in range(1, 10001):
    for _ in range(count[i]):
        sys.stdout.write(str(i) + '\n')
# https://www.acmicpc.net/problem/10989
