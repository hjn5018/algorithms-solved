import string

word = input().upper()
letter_list = [i for i in string.ascii_uppercase]
count_list = [0] * len(letter_list)
for letter in word:
    letter_index = letter_list.index(letter)
    count_list[letter_index] += 1
if count_list.count(max(count_list)) > 1:
    print('?')
else:
    max_index = count_list.index(max(count_list))
    print(letter_list[max_index])
# https://www.acmicpc.net/problem/1157
