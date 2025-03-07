N, 김지민_번호, 임한수_번호 = map(int, input().split())

# 홀수 개의 번호가 있는 순간,
# 마지막 번호를 가진 사람은
# 다음 홀수 개의 번호가 나올 때까지 부전승이다.

'''
1000 20 31
500 10 16
250 5 8
125 3 4
63 2 2
-> 4round
32
'''

def convert(n: int) -> int:
    if n % 2 == 0:
        n /= 2
        return n
    else:
        n += 1
        n /= 2
        return n

count = 0
while N != 1:
    # logic
    김지민_번호 = convert(김지민_번호)
    임한수_번호 = convert(임한수_번호)
    count += 1
    
    # 검사
    if 김지민_번호 == 임한수_번호:
        print(count)
        break
    
    # 마지막 단계
    N = convert(N)

# https://www.acmicpc.net/problem/1057
