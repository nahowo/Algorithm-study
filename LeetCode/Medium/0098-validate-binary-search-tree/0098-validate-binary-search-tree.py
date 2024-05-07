# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(root,minV,maxV):
            if root is None:
                return True
            
            return (minV<root.val<maxV and func(root.left,minV,root.val) and func(root.right,root.val,maxV))

        return func(root,(-1)*sys.maxsize,sys.maxsize)