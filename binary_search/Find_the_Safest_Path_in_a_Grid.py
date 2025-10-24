from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        answer = 0
        # 1. theif로부터 시작하는 BFS로 모든 grid에 대해서 safe 거리(가장 가까운 thief와의 거리) 구하기
        dists = [[float('inf')] * n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dists[i][j] = 0
                    q.append((i, j))

        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr >= n or nc < 0 or nc >= n or dists[nr][nc] != float('inf'):
                    continue
                dists[nr][nc] = dists[r][c] + 1
                q.append((nr, nc))
        
        # 3. BFS를 통해 (0, 0)에서 (n, n)까지의 route를 검증(기대 safe 거리 k보다 작아야 함)
        def is_valid_route(k):
            if dists[0][0] < k or dists[n-1][n-1] < k:
                return False
            r_q = deque([(0, 0)])
            visited = set()
            while r_q:
                r, c = r_q.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in visited or dists[nr][nc] < k:
                        continue
                    visited.add((nr, nc))
                    r_q.append((nr, nc))

        # 2. 최적의 safe 거리 k를 찾기 위해서 최악의 수와 0 사이에서 이분탐색
        left, right = 0, max(max(dists[row] for row in range(n)))
        while left <= right:
            mid = (left + right) // 2
            if is_valid_route(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
        
