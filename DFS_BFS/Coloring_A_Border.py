from collections import deque
from copy import deepcopy

class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        q = deque()
        m, n = len(grid), len(grid[0])
        new_grid = deepcopy(grid)
        visited = set()
        org_color = grid[row][col]
        q.append((row, col, org_color))
        dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
        
        while q:
            r, c, cur_color = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            # 경계 조건 1: 가장자리
            if cur_color == org_color and (r == 0 or c == 0 or r == m - 1 or c == n - 1):
                new_grid[r][c] = color
            for i in range(4):
                nr = r + dy[i]
                nc = c + dx[i]
                # list out of range 해결
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue
                # 경계 조건 2: 인접한 square의 색상이 다르다
                if grid[nr][nc] != org_color:
                    new_grid[r][c] = color
                    continue
                q.append((nr, nc, grid[nr][nc]))

        return new_grid
        
