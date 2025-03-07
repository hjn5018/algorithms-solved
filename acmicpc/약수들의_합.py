while True:
    n = int(input())
    # 입력이 -1이면 끝낸다.
    if n == -1:
        break
    
    # 약수를 전부 구한다.
    factor = []
    for i in range(1, n):
        if n % i == 0:
            factor.append(i)
    
    if sum(factor) == n:
        word = ''
        for i, v in enumerate(factor):
            if i != len(factor) - 1:
                word += f"{v} + "
            else:
                word += f"{v}"
        print(f"{n} = {word}")
    else:
        print(f"{n} is NOT perfect.")
# https://www.acmicpc.net/problem/9506
