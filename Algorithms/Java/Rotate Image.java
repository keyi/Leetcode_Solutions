public class Solution {
    public void rotate(int[][] matrix) {
		int length = matrix.length;
		for (int i = 0; i < length; i++) {
			for (int j = 0; j < length - i; j++)
				swap(matrix, i, j, length - j - 1, length - i - 1);
		}
		for (int i = 0; i < length / 2; i++)
			for (int j = 0; j < length; j++)
				swap(matrix, i, j, length - i - 1, j);
	}

	public void swap(int[][] matrix, int ai, int aj, int bi, int bj) {
		int temp = matrix[ai][aj];
		matrix[ai][aj] = matrix[bi][bj];
		matrix[bi][bj] = temp;
	}
}