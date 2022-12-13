public class Solution {
    public int MinFallingPathSum(int[][] matrix) {
        for (int r=matrix.Length-2; r>=0; r--) {
            for (int c=0; c<matrix.Length; c++) {
                int best = matrix[r+1][c];
                if (c > 0) {
                    best = Math.Min(best, matrix[r+1][c-1]);
                }
                if (c < matrix.Length-1) {
                    best = Math.Min(best, matrix[r+1][c+1]);
                }
                matrix[r][c] += best;
            }
        }
        int min_value = int.MaxValue;
        foreach (int x in matrix[0]) {
            min_value = Math.Min(min_value, x);
        }
        return min_value;
    }
}
