from itertools import combinations

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        for triplets in list(combinations(range(len(nums)), 3)):
            if nums[triplets[0]] != nums[triplets[1]] and nums[triplets[1]] != nums[triplets[2]] and nums[triplets[0]] != nums[triplets[2]]:
                answer += 1 
        
        return answer
        
