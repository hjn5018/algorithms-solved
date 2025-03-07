S = input()

'''
111 00 1 000 11 00처럼 단위별로 분해한다.
단위별로 개수를 센다.
최소 개수를 반환한다.
'''

list_ = []
prev = S[0]
str_ = ''
for i in S:
    if i != prev:
        list_.append(str_)
        str_ = ''
    str_ += i
    prev = i
list_.append(str_)

count_1 = 0
count_0 = 0
for i in list_:
    if '1' in i:
        count_1 += 1
    else:
        count_0 += 1

print(min(count_1, count_0))
# https://www.acmicpc.net/problem/1439
