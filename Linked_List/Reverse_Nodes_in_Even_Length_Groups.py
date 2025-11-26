from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        max_length = 2
        new_head = ListNode(head.val)
        cur_head = new_head
        head = head.next
        while head is not None:
            cur_length = 1
            q = deque()
            while cur_length <= max_length and head is not None:
                q.append((head.val))
                head = head.next
                cur_length += 1
            # print(q)
            if cur_length % 2 == 0:
                while q:
                    cur_head.next = ListNode(q.popleft())
                    cur_head = cur_head.next
            else:
                while q:
                    cur_head.next = ListNode(q.pop())
                    cur_head = cur_head.next
            max_length += 1
            # print(new_head)
        return new_head
