numbers = [i for i in range(1, 10001)]

def d(n: str):
    total = 0
    total += n
    for i in str(n):
        total += int(i)
    return total

d_numbers = {d(i) for i in numbers}

self_numbers = []
for i in numbers:
    if i in d_numbers:
        pass
    else:
        self_numbers.append(i)
# print(f"{self_numbers = }")

for i in self_numbers:
    print(i)
# https://www.acmicpc.net/problem/4673
