from collections import deque
'''
- stack을 사용해서 풀이(monotonic stack이라고도 함)
- 위치를 직접 확인할 방법이 없기 때문에 index를 stack에 같이 집어넣어야 함
- 변수 중복에 주의(덮어씌워짐)
'''
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = [0] * (10**4)
        stack = deque()
        cursor = 0
        while head is not None:
            if not stack or stack[-1][0] >= head.val:
                stack.append((head.val, cursor))
                cursor += 1
                head = head.next
                continue
            elif stack[-1][0] < head.val:
                while stack and stack[-1][0] < head.val:
                    _, node_cursor = stack.pop()
                    answer[node_cursor] = head.val

        return answer[:cursor]
            
