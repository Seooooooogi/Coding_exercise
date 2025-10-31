# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # p나 q가 LCA가 되는 경우
        if root in (None, p, q):
            return root
        # 아니라면 root의 좌측이나 우측을 후보군으로 두고 재귀적으로 탐색
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # left와 right가 모두 존재하면(p와 q를 모두 찾았으면) root가 LCA, 아니라면 계속 탐색
        if left and right:
            return root
        else:
            # left와 right 중에 None이 아닌 것을 반환
            return left or right
