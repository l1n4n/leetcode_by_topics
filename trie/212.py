# 212. Word Search II
# Given a 2D board and a list of words from the dictionary, find all words in the board.

# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

# Example:

# Input: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# Output: ["eat","oath"]

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = self.make_trie(words)
        
        self.res = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie, '')
        return list(self.res)
    
    def make_trie(self, words):
        t = {}
        for w in words:
            node = t
            for c in w:
                node = node.setdefault(c, {})
            node['#'] = True
        return t
    
    def dfs(self, board, i, j, trie, path):
        # end condition
        if '#' in trie:
            self.res.add(path)
        # out of boundary condition
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in trie:
            return        
        # process data at current level
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        c = board[i][j]
        board[i][j] = '*' # the same character cannot be used twice --> the starting c is crossed out
        for d in directions:
            self.dfs(board, i+d[0], j+d[1], trie[c], path+c)
        board[i][j] = c # restore
        