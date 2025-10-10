from collections import deque

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        answer = 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        # 초기조건 : 0번째 열과 0번째 행은 중간에 장애물이 없는 이상 unique path는 1개
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        # 장애물이 없다면 해당 위치에서의 dp는 위와 왼쪽의 경로의 수의 합으로 구성
        # 장애물이 있다면 해당 위치에서의 dp는 항상 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        
