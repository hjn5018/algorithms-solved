import sys
input = sys.stdin.readline

T = int(input())

is_prime = [True] * (1_000_001 + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(1_000_001**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, 1_000_001 + 1, i):
            is_prime[j] = False

for _ in range(T):
    N = int(input())

    partition_count = 0
    for n in range(2, N//2 + 1):
        if is_prime[n]:
            if is_prime[N - n]:
                partition_count += 1
    
    print(partition_count)
# https://www.acmicpc.net/problem/17103
