# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(Treenode):
            if Treenode == None:
                return 0

            lh = height(Treenode.left)
            rh = height(Treenode.right)
            if lh == -1 or rh == -1 : return - 1
            if abs(lh-rh)>1 : return - 1



            return max(lh,rh)+1    
        x = height(root)
        if x == -1: 
            return False
        else: return True    
