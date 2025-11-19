import heapq

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_hash = {}
        for i, j in enumerate(order):
            order_hash[j] = i
        new_order = []
        for k in s:
            if k in order_hash.keys():
                heapq.heappush(new_order, (order_hash[k], k))
            else:
                i += 1
                heapq.heappush(new_order, (i, k))
        answer = []
        while new_order:
            answer.append(heapq.heappop(new_order)[1])
        return "".join(answer)


from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []

        # 1) order에 정의된 순서대로 먼저 채움
        for ch in order:
            if ch in count:
                ans.append(ch * count[ch])
                del count[ch]

        # 2) 나머지 문자들(순서 정의 안 된 것들)은 그냥 뒤에 이어 붙이기
        for ch, cnt in count.items():
            ans.append(ch * cnt)

        return "".join(ans)
      
