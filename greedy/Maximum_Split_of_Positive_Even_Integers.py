class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # 짝수의 덧셈만으로는 홀수를 만들 수 없음
        if finalSum % 2 == 1:
            return []
        
        res = []
        curr = 2
        # 최소 단위부터 최대한으로 늘리기 위해 list에 추가
        while finalSum >= curr:
            res.append(curr)
            finalSum -= curr
            curr += 2

        # 나머지를 가장 큰 수에 더해줌(중복 회피)
        if finalSum > 0:
            res[-1] += finalSum

        return res
        
