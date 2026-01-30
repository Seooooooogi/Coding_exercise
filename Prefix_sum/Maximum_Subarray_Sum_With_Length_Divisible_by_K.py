class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        # 최댓값을 만드려면 누적합의 최솟값을 빼야 함
        # 즉, i % k == j % k 을 만족하는 조건에서 최솟값을 항상 유지하면 됨
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0

        answer = float('-inf')
        current_sum = 0
        n = len(nums)

        for i in range(n):
            current_sum += nums[i]
            rem = (i + 1) % k

            if min_prefix[rem] != float('-inf'):
                answer = max(answer, current_sum - min_prefix[rem])
            
            min_prefix[rem] = min(min_prefix[rem], current_sum)
        
        return answer
        
