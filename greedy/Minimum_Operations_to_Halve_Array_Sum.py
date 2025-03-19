import heapq

# 항상 최대 수를 반절하는 것이 최선
# 최대 힙 활용(음수를 집어넣어서 최대로 만들어줌)
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_num = sum(nums)
        goal = total_num / 2
        answer = 0
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
    
        while total_num > goal:
            largest = heapq.heappop(heap)
            largest /= 2
            total_num += largest
            heapq.heappush(heap, largest)
            answer += 1
        return answer
