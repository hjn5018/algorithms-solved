def is_point_in_planet(P:dict, x:int, y:int, r:int) -> bool:
    if (P['x'] - x)**2 + (P['y'] - y)**2 < r**2:
        return True
    return False
    
T = int(input())
for _ in range(T):
    S = {'x':0, 'y':0}
    E = {'x':0, 'y':0}
    S['x'], S['y'], E['x'], E['y'] = map(int, input().split())
    
    N = int(input())
    set_s = set()
    set_e = set()
    for i in range(N):
        x, y, r = map(int, input().split())
        if is_point_in_planet(S, x, y, r):
            set_s.add(i)
        if is_point_in_planet(E, x, y, r):
            set_e.add(i)
    
    result = len(set_s | set_e) - len(set_s & set_e)
    print(result)
# https://www.acmicpc.net/problem/1004
