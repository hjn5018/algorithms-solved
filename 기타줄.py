N, M = map(int, input().split())

list_ = []
for _ in range(M):
    list_.append(list(map(int, input().split())))

package = min([list_[i][0] for i in range(M)])
piece = min([list_[i][1] for i in range(M)])

if 6 * piece <= package:
    print(N * piece)
elif 6 * piece > package:
    result = 0
    result += (N // 6) * package
    if (N % 6) * piece <= package:
        result += (N % 6) * piece
    else:
        result += package
    print(result)

# https://www.acmicpc.net/problem/1049
