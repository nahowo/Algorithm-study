# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def func(root,d,depth):
            if root==None:
                return 0
            depth=max(func(root.left,d+1,depth),func(root.right,d+1,depth),d)
            return depth
        
        depth=func(root,1,1)
        return depth