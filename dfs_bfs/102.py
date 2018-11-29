# 102. Binary Tree Level Order Traversal
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. BFS
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        ans = []
        q = deque([root])
        
        while q:
            current_level, size = [], len(q)
            for _ in range(size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(current_level)      
        
        return ans
# 2. DFS
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.ans = []
        self._dfs(root, 0)
        return self.ans
    
    def _dfs(self, node, level):        
        if not node:
            return []        
               
        if len(self.ans) < level+1:
            self.ans.append([])
        
        self.ans[level].append(node.val)
        
        self._dfs(node.left, level+1)
        self._dfs(node.right, level+1)       