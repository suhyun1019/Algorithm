"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None :
            return 0
        
        q=collections.deque([root])
        depth=0
        
        while q :
            depth+=1
            for i in range(len(q)) :
                node=q.popleft()
                if node.left :
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
        
        return depth
