// 36. Valid Sudoku
// Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.


class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][10]; 
        boolean[][] cols = new boolean[9][10];
        boolean[][] blks = new boolean[9][10];
        
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char c = board[i][j];
                if (c == '.') {
                    continue;
                }
                int cur = (int)(c - '0');
                if (rows[i][cur]) {
                    return false;
                } else {
                    rows[i][cur] = true;
                }
                if (cols[j][cur]) {
                    return false;
                } else {
                    cols[j][cur] = true;
                }
                if (blks[i/3*3+j/3][cur]) {
                    return false;
                } else {
                    blks[i/3*3+j/3][cur] = true;
                }
            }
        }
        return true;
    }
}