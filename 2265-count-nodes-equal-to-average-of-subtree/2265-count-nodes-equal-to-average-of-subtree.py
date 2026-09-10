# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.result = 0
        
        def dfs(root):
            if root is None:
                return 0, 0
            
            # Get sum and count from left subtree
            left_sum, left_count = dfs(root.left)
            
            # Get sum and count from right subtree
            right_sum, right_count = dfs(root.right)
            
            # Calculate sum of current subtree
            total_sum = root.val + left_sum + right_sum
            
            # Calculate number of nodes in current subtree
            total_count = 1 + left_count + right_count
            
            # Check if node value equals subtree average
            if root.val == total_sum // total_count:
                self.result += 1
            
            # Return sum and count to parent node
            return total_sum, total_count
        
        dfs(root)
        return self.result