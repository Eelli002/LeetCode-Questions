# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Is_Same(self, r, sr):
            if not r and not sr: 
                print('3')
                return True
            if not r or not sr or r.val != sr.val: 
                print('4')
                return False
            return (self.Is_Same(r.left, sr.left) and self.Is_Same(r.right, sr.right))
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: 
            print('1')
            return False
        
        print("root.val: ", root.val)
        
        if self.Is_Same(root, subRoot): 
            print('2')
            return True
        
        return self.isSubtree(root.left, subRoot) | self.isSubtree(root.right, subRoot)