def solution(dirs):
    x, y = 0, 0
    visited = set()
    d1 = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

    for dir in dirs:
        dx, dy = d1[dir]
        nx, ny = x + dx, y + dy
        if nx < -5 or nx > 5:
            continue
        elif ny < -5 or ny > 5:
            continue
        go = (x, y, nx, ny)
        back = (nx, ny, x, y)
        x, y = nx, ny
        if go not in visited:
            visited.add(go)
            visited.add(back)

    return len(visited) / 2

print(solution("ULURRDLLU"))
# 10x10 행렬
# 각 좌표에 -5를해서 구해보자.

# "ULURRDLLU"	7