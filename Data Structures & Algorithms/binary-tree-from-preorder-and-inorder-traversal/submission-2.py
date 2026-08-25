class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(val)
            mid = inorder_idx[val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)