n = int(input())

f = [0]*max(4, n+1)
f[1] = f[2] = f[3] = 1

for i in range(4, n+1):
    f[i] = f[i-1] + f[i-3]
    
print(f[n])

# https://www.acmicpc.net/problem/14495
