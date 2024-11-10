N, K = map(int, input().split())
notes = [input().split() for _ in range(K)]
wheel = ['?'] * N
visited = set()
# Set the starting letter
pos = 0
wheel[pos] = notes[-1][1]

# Traverse notes in reverse order
for i in range(K - 1, 0, -1):
    pos = (pos + int(notes[i][0])) % N
    letter = notes[i - 1][1]
    
    if wheel[pos] == '?':  # Fill the slot if empty
        if letter in visited:
            wheel = ['!']
            break
        wheel[pos] = letter
        visited.add(letter)
    elif wheel[pos] != letter:  # Conflict in the slot
        wheel = ['!']
        break

print(''.join(wheel))

# https://www.acmicpc.net/problem/2840
