A, B = input().split()

min_diff = len(A)
for i in range(len(B)-len(A)+1):
    diff = 0
    for j in range(len(A)):
        if A[j] == B[j+i]:
            pass
        elif A[j] != B[j+i]:
            diff += 1
    if diff < min_diff:
        min_diff = diff
print(min_diff)
# https://www.acmicpc.net/problem/1120
