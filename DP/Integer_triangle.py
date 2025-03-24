# 1. top-down 방식
def solution(triangle):
    n = len(triangle)
    dp = [[0] * i for i in range(1, n+1)]
    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    
    return max(dp[-1])


# 2. bottom-up 방식
def solution(triangle):
    
    n = len(triangle)
    dp = [[0] * i for i in range(1, n+1)]
    for i in range(n):
        dp[-1][i] = triangle[-1][i]
    
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j] + triangle[i][j], dp[i+1][j+1] + triangle[i][j])
    
    return dp[0][0]
