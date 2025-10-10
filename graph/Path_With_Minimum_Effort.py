import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        m, n = len(heights), len(heights[0])
        # 변형된 다익스트라 알고리즘
        # dist가 effort의 역할을 맡음
        dists = [[float('inf')] * n for _ in range(m)]
        h = [(0, 0, 0)]
        while h:
            effort, y, x = heapq.heappop(h)
            # 우하단이 목적지이므로 도착했을 때는 이미 최소 effort
            if y == m - 1 and x == n - 1:
                return effort
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < m and  0 <= nx < n:
                    new_effort = max(effort, abs(heights[ny][nx] - heights[y][x]))
                    if dists[ny][nx] > new_effort:
                        dists[ny][nx] = new_effort
                        heapq.heappush(h, (new_effort, ny, nx))
        
