# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result:List[int]=[]
        def loop(r: Optional[TreeNode]):
            if not r:
                return

            loop(r.left)
            loop(r.right)
            result.append(r.val)


        loop(root)    
        return result
        