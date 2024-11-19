S = input()

in_tag = False
result = ""
tmp = ""
for i in range(len(S)):
    if S[i] == '<':
        if tmp:
            result += tmp[::-1]
            tmp = ""
        in_tag = True
        result += '<'
        continue
    if in_tag:
        result += S[i]
        if S[i] == '>':
            in_tag = False
        continue

    if S[i] != ' ':
        tmp += S[i]
    else:
        result += tmp[::-1]
        result += ' '
        tmp = ""
    
    if i == len(S)-1:
        result += tmp[::-1]

print(result)
# https://www.acmicpc.net/problem/17413
