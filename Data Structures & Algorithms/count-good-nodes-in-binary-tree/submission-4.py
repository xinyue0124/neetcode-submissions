# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            if not node:
                return 0
            good = 1 if  node.val >= path_max else 0
            path_max = max(path_max, node.val)
            good += dfs(node.left, path_max)
            good += dfs(node.right, path_max)
            return good
       
        return dfs(root, root.val)
