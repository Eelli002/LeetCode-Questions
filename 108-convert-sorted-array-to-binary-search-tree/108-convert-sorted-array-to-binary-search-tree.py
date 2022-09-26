# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def BST(nums):
            if not nums: return None
            
            r = len(nums)
            mp = r // 2
            print('values:', nums)
            print('mp:', nums[mp])
            
            
            root = TreeNode(nums[mp])
            root.left = BST(nums[:mp])
            root.right = BST(nums[mp+1:])
            
            return root
        
        return BST(nums)
            