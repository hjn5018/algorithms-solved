N, taesoo, P = map(int, input().split())
if N == 0:
    print(1)
else:
    scores = list(map(int, input().split()))

    if N == P:
        if taesoo <= scores[-1]:
            print(-1)
        else:
            scores.append(taesoo)
            scores.sort(reverse=True)
            scores = scores[:-1]
            count = 0
            for score in scores:
                if score > taesoo:
                    count += 1
            print(count+1)
    else:
        scores.append(taesoo)
        scores.sort(reverse=True)
        scores = scores[:-1]
        count = 0
        for score in scores:
            if score > taesoo:
                count += 1
        print(count+1)
# https://www.acmicpc.net/problem/1205
