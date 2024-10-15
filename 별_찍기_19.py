N = int(input())

as_is = ''
def gen(N:int, as_is:str) -> str:
    to_be = ''
    if N == 1:
        to_be += '*'
    else:
        to_be += '*' * (4*N-3)
        to_be += '\n'
        to_be += '*'
        to_be += ' ' * (4*N-5)
        to_be += '*'
        to_be += '\n'
        for i in range(4*N-7):
            to_be += '* '
            to_be += as_is.split('\n')[i]
            to_be += ' *'
            to_be += '\n'
        to_be += '*'
        to_be += ' ' * (4*N-5)
        to_be += '*'
        to_be += '\n'
        to_be += '*' * (4*N-3)
    as_is = to_be
    return as_is

for i in range(1, N+1):
    as_is = gen(i, as_is)

print(as_is)
# https://www.acmicpc.net/problem/10994
