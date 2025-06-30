class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [0] * (n+1)
        # 최악의 경우 : 자기 자신만큼 operation을 행함
        for i in range(2, n+1):
            dp[i] = i
            # 자신의 약수가 범위 내에 존재하는 경우 : 약수까지 걸리는 operation에서 배수만큼 더 operation을 행함
            for j in range(i-1, 0, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break
        return dp[n]
        
