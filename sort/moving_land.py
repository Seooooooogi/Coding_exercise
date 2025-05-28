import heapq

def solution(land, height):
    answer = 0
    n = len(land)
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * n for _ in range(n)]
    q = []
    # heap으로 최소 cost의 경로부터 answer에 추가
    # 비효율적인 cost 경로는 BFS를 통해 갱신하지 않도록 함
    heapq.heappush(q, [0, 0, 0])

    # BFS 구현 부분
    while q:
        cost, y, x = heapq.heappop(q)
        if not visited[y][x]:
            visited[y][x] = True
            answer += cost
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                # 대부분의 out of range 문제는 제약조건을 잘못 설정하는 데서 옴
                if 0 <= nx < n and 0 <= ny < n:
                    cost_diff = abs(land[ny][nx] - land[y][x])
                    if cost_diff > height:
                        new_cost = cost_diff
                    else:
                        new_cost = 0
                    heapq.heappush(q, [new_cost, ny, nx])
                
    return answer
  
