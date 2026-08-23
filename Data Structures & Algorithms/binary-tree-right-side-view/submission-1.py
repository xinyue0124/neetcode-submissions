# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def f(node, depth):
            if not node:
                return None
            if len(res) == depth:
                res.append(node.val)
            f(node.right, depth + 1)
            f(node.left, depth + 1)
        f(root, 0)
        return res