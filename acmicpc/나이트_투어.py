from pprint import pprint

positions = [input() for _ in range(36)]
for i in range(36):
    positions[i] = [ord(positions[i][0])-65, int(positions[i][1])-1]

def find(positions):
    visited = [[False] * 6 for _ in range(6)]
    possible_route = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))

    visited[positions[0][0]][positions[0][1]] = True
    for i in range(35):
        possible_positions = []
        for dx, dy in possible_route:
            if 0 <= positions[i][0] + dy <= 5 and 0 <= positions[i][1] + dx <= 5:
                possible_positions.append([positions[i][0] + dy, positions[i][1] + dx])
        if [positions[i+1][0], positions[i+1][1]] in possible_positions:
            if not visited[positions[i+1][0]][positions[i+1][1]]:
                visited[positions[i+1][0]][positions[i+1][1]] = True
            else:
                return "Invalid"
        else:
            return "Invalid"
    
    for i in range(6):
        if not all(visited[i]):
            return "Invalid"
        
    start_x, start_y = positions[0]
    end_x, end_y = positions[35]
    if [start_x, start_y] not in [[end_x + dx, end_y + dy] for dx, dy in possible_route]:
        return "Invalid"  # 시작과 끝이 연결되지 않음
    
    return "Valid"

print(find(positions))
# https://www.acmicpc.net/problem/1331
