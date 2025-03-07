word = input()

count = 0
for i, letter in enumerate(word):
    count += 1
    if i < len(word) - 1:
        if letter == 'c':
            if word[i+1] == '=' or word[i+1] == '-':
                count -= 1
        if letter == 'd':
            if word[i+1] == '-':
                count -= 1
        if letter == 's':
            if word[i+1] == '=':
                count -= 1
        if letter == 'l' or letter == 'n':
            if word[i+1] == 'j':
                count -= 1
        if letter == 'z':
            if word[i-1] == 'd' and word[i+1] == '=':
                count -= 2
            elif word[i+1] == '=':
                count -= 1
print(count)
 # https://www.acmicpc.net/problem/2941
