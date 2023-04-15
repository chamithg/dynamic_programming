# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n):
        if n % 2 == 0:
            return None
        output = set()

        def create(count,head_root,root):
            main_root = head_root[:]
            if not root or count < 2:
                output.add(main_root)
                return
            root.left = TreeNode()
            root.right = TreeNode()
            count -=2

            create(count,main_root,root.left)
            create(count,main_root,root.right)




        
        root = TreeNode()
        create(n-1,root,root)

        return output