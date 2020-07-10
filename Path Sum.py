# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None: 
            return False 
  
        else: 
            ans = 0          
        
            subSum = s - root.val  
          
          
            if(subSum == 0 and root.left == None and root.right == None): 
                return True 
  
            if root.left is not None: 
                ans = ans or self.hasPathSum(root.left, subSum) 
            
            if root.right is not None: 
                ans = ans or self.hasPathSum(root.right, subSum) 
  
            return ans  