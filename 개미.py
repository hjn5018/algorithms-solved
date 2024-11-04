N1, N2 = map(int, input().split())
G1 = input()
G2 = input()
T = int(input())

G1 = [(G1[i], 'R') for i in range(N1)]
G2 = [(G2[i], 'L') for i in range(N2)]
G1 = G1[::-1]
L = G1 + G2

for _ in range(T):
    LL = L[:]
    for i in range(N1+N2):
        if i+1<N1+N2 and L[i][1] == 'R' and L[i+1][1] == 'L':
            LL[i], LL[i+1] = LL[i+1], L[i]
    L = LL[:]

result = [L[i][0] for i in range(N1+N2)]
print(''.join(result))
# https://www.acmicpc.net/problem/3048
