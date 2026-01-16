# 1. heapq를 이용한 풀이

import heapq

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        answer = sum(reward2)
        cur = 0
        reward_heap = []
        for i, (v1, v2) in enumerate(zip(reward1, reward2)):
            heapq.heappush(reward_heap, ((-v1+v2), i))
        while cur < k:
            v, i = heapq.heappop(reward_heap)
            answer += -v
            cur += 1

        return answer
        
 # sort를 이용한 풀이
 
 class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        answer = sum(reward2)
        diff = []
        for v1, v2 in zip(reward1, reward2):
            diff.append(v1 - v2)
        diff.sort(reverse=True)

        for i in range(k):
            answer += diff[i]

        return answer
