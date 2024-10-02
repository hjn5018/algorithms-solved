N = int(input())

trees = [int(input()) for _ in range(N)]

gaps = []
for i in range(len(trees)-1):
    gap = trees[i+1] - trees[i]
    gaps.append(gap)
    
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a%b
    return a

gcd_ = gcd(gaps[0], gaps[1])
idx = 2
while idx < len(gaps):
    gcd_ = gcd(gcd_, gaps[idx])
    idx += 1

# gcd_ at this line means gcd of all gaps

count = 0
for gap in gaps:
    count += (gap // gcd_) - 1
print(count)

# https://www.acmicpc.net/problem/2485
