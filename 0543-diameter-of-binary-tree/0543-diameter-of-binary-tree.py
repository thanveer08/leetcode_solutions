# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxi = 0
        def balanced(node):
            nonlocal maxi
            if node == None:
                return 0
            left = balanced(node.left)
            right = balanced(node.right)

            maxi = max(maxi,left+right)
            return 1 + max(left,right)    
        balanced(root)
        return maxi   