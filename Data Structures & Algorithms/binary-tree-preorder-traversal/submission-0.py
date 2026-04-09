# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result:List[int]=[]
        def loop(r: Optional[TreeNode]):
            if not r:
                return

            result.append(r.val)
            loop(r.left)
            loop(r.right)


        loop(root)    
        return result
