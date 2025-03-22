from collections import deque

def solution(maps):
    m, n = len(maps), len(maps[0])
    for i in range(m):
        for j in range(n):
            if maps[i][j] == "S":
                start_x, start_y = j, i
            if maps[i][j] == "L":
                lever_x, lever_y = j, i
            if maps[i][j] == "E":
                end_x, end_y = j, i
                
    def bfs(start_x, start_y, end_x, end_y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        q = deque()
        q.append((start_y, start_x, 0))
        visited = [[False] * n for _ in range(m)]
        visited[start_y][start_x] = True
        while q:
            y, x, time = q.popleft()
            if x == end_x and y == end_y:
                return time
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if ny < 0 or ny >= m or nx < 0 or nx >= n or visited[ny][nx] == True:
                    continue
                if maps[ny][nx] == "X":
                    continue
                visited[ny][nx] = True
                q.append((ny, nx, time+1))
        return -1

    # 레버에 도착하기까지 최단거리를 bfs로 구하고, 레버에서 출구까지의 최단거리를 bfs로 구함
    # visited를 별도로 해야 하는 이유는 통로를 여러번 왔다갔다할 수 있기 때문. 즉 출구를 지나서 레버로 도착하는 테스트케이스도 존재함
    lever_time = bfs(start_x, start_y, lever_x, lever_y)
    end_time = bfs(lever_x, lever_y, end_x, end_y)
    if lever_time == -1 or end_time == -1:
        return -1
    return lever_time + end_time
