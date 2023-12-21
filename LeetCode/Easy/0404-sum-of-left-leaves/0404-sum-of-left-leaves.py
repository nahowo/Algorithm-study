# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # left leaf 조건:
        # 1) 부모의 왼쪽 자식
        # 2) 자식이 없음
        
        def check(node, potent):
            if not node:
                return 0
            elif not node.left and not node.right:
                if potent:
                    return node.val
                else:
                    return 0
            return check(node.left,True) + check(node.right, False)
        
        return check(root, False)