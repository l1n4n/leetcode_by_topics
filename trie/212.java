class Solution {
    public List<String> findWords(char[][] board, String[] words) {
        List<String> res = new ArrayList<>();
        TrieNode root = buildTrie(words);
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                dfs(board, i, j, root, res);
            }
        }
        return res;
        
    }
    
    public TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String s: words) {
            TrieNode ws = root;
            for (char c: s.toCharArray()) {
                int i = c - 'a';
                if (ws.kids[i] == null) {
                    ws.kids[i] = new TrieNode();
                }
                ws = ws.kids[i];
            }
            ws.word = s; 
        }
        return root;
    }
    
    class TrieNode {
        TrieNode[] kids = new TrieNode[26];
        String word;
    }
    
    public void dfs(char[][] board, int i, int j, TrieNode node, List<String> res) {
        // stop condition
        char c = board[i][j];
        if (c == '#' || node.kids[c - 'a'] == null) return;
        // process
        node = node.kids[c - 'a'];
        if (node.word != null) {
            res.add(node.word);
            node.word = null; // de-duplicate
        }
        // recursion
        board[i][j] = '#';
        if (i > 0) dfs(board, i-1, j, node, res);
        if (j > 0) dfs(board, i, j-1, node, res);
        if (i < board.length - 1) dfs(board, i+1, j, node, res);
        if (j < board[0].length - 1) dfs(board, i, j+1, node, res);
        board[i][j] = c;
        
    }
}