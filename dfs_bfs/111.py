# 111. Minimum Depth of Binary Tree
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS
## CAVEAT: return answer only when the current node has no kid

from collections import deque
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        q = deque([root])
        mind = 0
        while q:
            mind += 1
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if not node.left and not node.right:
                    return mind
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return mind

# DFS Recursion
## CAVEAT: when the current node has only one kid, travel down this kid's branch
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if root.left and not root.right: return 1+self.minDepth(root.left)
        elif root.right and not root.left: return 1+self.minDepth(root.right)
        else: return 1+min(self.minDepth(root.left), self.minDepth(root.right))

# DFS Iteration
## To find the min, init ans = float('inf')
## if the current node has no kid, update ans
## put a kid into stack only if it is not null
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        stack = [(root, 1)]
        dep = float('inf')
        
        while stack:
            node, level = stack.pop()
            kids = [node.left, node.right]
            if not any(kids):
                dep = min(dep, level)
            for k in kids:
                if k: stack.append((k, level+1))
            
        return dep

###############################################################
# dfs's stack has tuples (node, level) for recording depth info