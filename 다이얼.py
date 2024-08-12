word = input()
answer = 0

for letter in word:
    if letter == 'A' or letter == 'B' or letter == 'C':
        answer += 3
    elif letter == 'D' or letter == 'E' or letter == 'F':
        answer += 4
    elif letter == 'G' or letter == 'H' or letter == 'I':
        answer += 5
    elif letter == 'J' or letter == 'K' or letter == 'L':
        answer += 6
    elif letter == 'M' or letter == 'N' or letter == 'O':
        answer += 7
    elif letter == 'P' or letter == 'Q' or letter == 'R' or letter == 'S':
        answer += 8
    elif letter == 'T' or letter == 'U' or letter == 'V':
        answer += 9
    elif letter == 'W' or letter == 'X' or letter == 'Y' or letter == 'Z':
        answer += 10

print(answer)

# https://www.acmicpc.net/problem/5622
