M = int(input())
N = int(input())
primes = []

# M부터 N까지 수를 확인한다.
for i in range(M, N+1):
    if i == 1:
        continue
    
    # i보다 작은 수들을 i와 대조한다.
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
            break # i의 약수가 하나라도 존재한다면 탐색을 중단한다.
    
    # i를 배수로 하는 j가 없다면 i는 약수이다.
    if count == 0:
        primes.append(i)

if primes == []:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])
# https://www.acmicpc.net/problem/2581
