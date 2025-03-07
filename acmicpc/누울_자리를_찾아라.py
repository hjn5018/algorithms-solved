N = int(input())

room = [input() for _ in range(N)]
inverted_room = [''.join(i) for i in zip(*room)]

def find_place(line: str) -> int:
    arr = line.split('X')
    count = 0
    for i in arr:
        if '..' in i:
            count += 1
    return count

row_count, column_count = 0, 0
for line in room:
    line_count = find_place(line)
    row_count += line_count

for line in inverted_room:
    line_count = find_place(line)
    column_count += line_count

print(f"{row_count} {column_count}")
# https://www.acmicpc.net/problem/1652
