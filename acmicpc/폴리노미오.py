board = input()
splited = board.split('.')

result = []
flag = True
for i in splited:
    if i == '':
        result.append('')
    else:
        if len(i) == 2:
            result.append('BB')
        elif len(i) % 4 == 0:
            result.append('A'*len(i))
        elif len(i) % 4 == 2:
            result.append('A'*(len(i)-2) + 'BB')
        else:
            flag = False
            break
result = '.'.join(result)
print(result) if flag else print(-1)
# https://www.acmicpc.net/problem/1343
