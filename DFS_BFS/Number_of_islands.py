class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(y, x):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위 0 이상인 것으로 체크하기
                if ny >= 0 and ny < m and nx >= 0 and nx < n and (ny, nx) not in visited and grid[ny][nx] == "1":
                    visited.add((ny, nx))
                    dfs(ny, nx)

        m, n = len(grid), len(grid[0])
        visited = set()
        answer = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    visited.add((i, j))
                    answer += 1
                    dfs(i, j)
        return answer
