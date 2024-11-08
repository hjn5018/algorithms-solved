def sieve_of_eratosthenes(limit):
    # 에라토스테네스의 체로 소수 리스트를 생성
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [x for x in range(2, limit + 1) if primes[x]]

def find_prime_sum(K, primes):
    # 3개의 소수 합으로 K를 만들 수 있는지 확인
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            for k in range(j, len(primes)):
                if primes[i] + primes[j] + primes[k] == K:
                    return [primes[i], primes[j], primes[k]]
    return [0]

def main():
    # 최대 K값은 999이므로, 1000 이하의 소수 구하기
    primes = sieve_of_eratosthenes(1000)
    
    T = int(input())  # 테스트 케이스 수
    for _ in range(T):
        K = int(input())  # 홀수 K 입력
        result = find_prime_sum(K, primes)
        if result == [0]:
            print(0)
        else:
            print(*sorted(result))

if __name__ == "__main__":
    main()

# https://www.acmicpc.net/problem/11502
