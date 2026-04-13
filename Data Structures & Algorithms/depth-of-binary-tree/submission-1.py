# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[root]
        dep=0
        while stack:
            dep +=1
            level=[]
            while stack:
                level.append(stack.pop())
            c=[]

            for p in level:
                if p.left:
                    c.append(p.left)
                if p.right:
                    c.append(p.right)

            stack +=c        

        return dep
