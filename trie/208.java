class TrieNode {
    public char val;
    public TrieNode[] children = new TrieNode[26];
    public boolean isEnd;
    public TrieNode() {}
    public TrieNode(char c) {
        TrieNode node = new TrieNode();
        node.val = c;
    }
}
class Trie {

    /** Initialize your data structure here. */
    private TrieNode root;    
    public Trie() {
        root = new TrieNode(' ');
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode start = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (start.children[c - 'a'] == null) {
                start.children[c - 'a'] = new TrieNode(c);
            }
            start = start.children[c - 'a'];
        }
        start.isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode start = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (start.children[c - 'a'] == null) {
                return false;
            }
            start = start.children[c - 'a'];
        }
        return start.isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode start = root;
        for (int i = 0; i < prefix.length(); i++) {
            char c = prefix.charAt(i);
            if (start.children[c - 'a'] == null) {
                return false;
            }
            start = start.children[c - 'a'];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */