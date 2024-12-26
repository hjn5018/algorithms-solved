def count_paper(x, y, size):
    global white, blue
    color = paper[x][y]  # 시작점의 색상
    
    # 현재 종이가 모두 같은 색인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                # 4개의 하위 영역으로 분할
                half = size // 2
                count_paper(x, y, half)
                count_paper(x, y + half, half)
                count_paper(x + half, y, half)
                count_paper(x + half, y + half, half)
                return
    
    # 모두 같은 색이면 해당 색 카운트 증가
    if color == 0:
        white += 1
    else:
        blue += 1


# 입력 처리
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

# 결과 변수
white = 0
blue = 0

# 시작
count_paper(0, 0, N)

# 출력
print(white)
print(blue)

# https://www.acmicpc.net/problem/2630
