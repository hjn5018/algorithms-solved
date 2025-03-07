T = int(input())

def is_prime(n:int) -> bool:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    target = n//2
    while target:
        if is_prime(target) & is_prime(n-target):
            print(f"{target} {n-target}")
            break
        else:
            target -= 1
# https://www.acmicpc.net/problem/9020
