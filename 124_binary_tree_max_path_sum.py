# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root.left and not root.right:
            return root.val

        self.max_sum = float(-inf)
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            self.max_sum = max(self.max_sum,root.val + l, root.val + r, root.val + l + r, root.val)
            return max(root.val + l, root.val + r,root.val)

        
        dfs(root)
        return self.max_sum