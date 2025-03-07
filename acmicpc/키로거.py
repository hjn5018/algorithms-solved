T = int(input())
for _ in range(T):
    log = input()
    left = []   # 커서 왼쪽 리스트
    right = []  # 커서 오른쪽 리스트
    for l in log:
        if l not in ('<', '>', '-'):
            left.append(l)  # 왼쪽 리스트에 문자 삽입
        elif l == '<' and left:
            right.append(left.pop())  # 왼쪽 리스트에서 하나 뽑아서 오른쪽으로 이동
        elif l == '>' and right:
            left.append(right.pop())  # 오른쪽 리스트에서 하나 뽑아서 왼쪽으로 이동
        elif l == '-' and left:
            left.pop()  # 왼쪽 리스트에서 문자 삭제
    print(''.join(left + right[::-1]))  # 왼쪽 리스트와 오른쪽 리스트를 합쳐서 출력

# https://www.acmicpc.net/problem/5397
