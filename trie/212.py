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
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

END_OF_WORD = "#"

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]: return []
        if not words: return []

        root = self._trie(words)
        
        self.res = set()
        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                self._dfs(board, i, j, root, '')
        return list(self.res)
    
    def _trie(self, words):
        t = {}
        for w in words:
            node = t
            for c in w:
                node = node.setdefault(c, {})
            node[END_OF_WORD] = END_OF_WORD
        return t
    
    def _dfs(self, board, i, j, trie, path):
        # end condition
        if END_OF_WORD in trie:
            self.res.add(path)
        # out of boundary condition
        if i < 0 or i >= self.m  \
        or j < 0 or j >= self.n \
        or board[i][j] not in trie:
            return        
        # process data at current level
        tmp, board[i][j] = board[i][j], '*' # the same character cannot be used twice --> the starting char is crossed out
        for k in range(4):
            self._dfs(board, i+dx[k], j+dy[k], trie[tmp], path+tmp)
        board[i][j] = tmp # restore

