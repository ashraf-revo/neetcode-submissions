# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def is_equal(self,t1: Optional[TreeNode], t2: Optional[TreeNode]):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False

        return t1.val ==t2.val and  self.is_equal(t1.left,t2.left) and self.is_equal(t1.right,t2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:



        if self.is_equal(root,subRoot):
            return True

        if root.left and self.isSubtree(root.left,subRoot):
            return True

        if root.right and self.isSubtree(root.right,subRoot):
            return True

        return False

        


            