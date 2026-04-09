# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result:List[int]=[]
        def loop(r: Optional[TreeNode]):
            if not r:
                return

            loop(r.left)
            result.append(r.val)
            loop(r.right)


        loop(root)    
        return result
        