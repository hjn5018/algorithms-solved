def recursion(s, l, r, count):
    if l >= r: return [1, count]
    elif s[l] != s[r]: return [0, count]
    else:
        count += 1
        return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, count=1)

N = int(input())
for _ in range(N):
    s = input()
    result = isPalindrome(s)
    print(*result)
# https://www.acmicpc.net/problem/25501
