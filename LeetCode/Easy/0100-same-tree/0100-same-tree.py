# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q and p.val==q.val: # p and q are both Not None and have same value
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return not p and not q # p and q are both None