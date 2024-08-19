word_list = [input() for _ in range(5)]
word_len_list = list(map(len, word_list))
max_len = max(word_len_list)
answer = ''
for i in range(max_len):
    for j in range(5):
        if word_len_list[j] > i:
            answer += word_list[j][i]
print(answer)
# https://www.acmicpc.net/problem/10798
