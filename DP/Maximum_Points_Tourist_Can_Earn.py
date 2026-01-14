class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        # k : 행동 가능한 일수, n : 도시 수
        dp = [[0] * n for _ in range(k+1)]

        # day 0
        for curr in range(n):
            # 1. 그 자리에 머무는 경우
            dp[0][curr] = max(dp[0][curr], stayScore[0][curr])
            # 2. 이동하는 경우
            for dest in range(n):
                if curr != dest:
                    dp[0][dest] = max(dp[0][dest], travelScore[curr][dest])

        # day 1 ~ day k
        for i in range(1, k):
            for curr in range(n):
                # 1. 그 자리에 머무는 경우
                dp[i][curr] = max(dp[i][curr], dp[i-1][curr] + stayScore[i][curr])
                # 2. 이동하는 경우
                for dest in range(n):
                    if curr != dest:
                        dp[i][dest] = max(dp[i][dest], dp[i-1][curr] + travelScore[curr][dest])

        return max(dp[k-1])
