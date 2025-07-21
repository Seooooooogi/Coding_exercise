class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # dp[i][j] : 꼭짓점 i부터 j까지의 부분 삼각형을 삼각 분할했을 때의 최소 점수
        # 중간에 k를 선택하면서(i < k < j) i부터 k까지의 부분 분할 문제, k부터 j까지의 부분 분할 문제 해결
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[j] * values[k]
                    if cost < dp[i][j]:
                        dp[i][j] = cost
        
        return dp[0][n-1]
        
