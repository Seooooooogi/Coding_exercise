from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        answer = []
        q = deque()
        q.append(root1)
        q.append(root2)
        while q:
            root = q.pop()
            if root is None:
                continue
            answer.append(root.val)
            q.append(root.left)
            q.append(root.right)

        return sorted(answer)
