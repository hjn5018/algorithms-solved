from pprint import pprint

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
# pprint(paper)

def search(x, y, size):
    global pair
    start_value = paper[x][y]
    same = True

    for i in range(size):
        for j in range(size):
            if paper[x + i][y + j] != start_value:
                same = False
                break
        if not same:
            break
    
    if same:
        pair[start_value] += 1
    else:
        new_size = size // 3
        for k in range(3):
            for l in range(3):
                search(x + k * new_size, y + l * new_size, new_size)

pair = {-1:0, 0:0, 1:0}
search(0, 0, N)

print(pair[-1])
print(pair[0])
print(pair[1])
# https://www.acmicpc.net/problem/1780
