def solution(strings, n):
    sort1 = sorted(strings)
    return sorted(sort1, key=lambda x:x[n])

# 
