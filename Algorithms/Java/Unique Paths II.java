public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
		int n = obstacleGrid[0].length;
		int[][] num = new int[m][n];
		for (int i = 0; i < m; i++) {
			if (obstacleGrid[i][0] != 1)
				num[i][0] = 1;
			else
				break;
		}
		for (int j = 0; j < n; j++) {
			if (obstacleGrid[0][j] != 1)
				num[0][j] = 1;
			else
				break;
		}
		for (int i = 1; i < m; i++) {
			for (int j = 1; j < n; j++) {
				if (obstacleGrid[i][j] == 1)
					num[i][j] = 0;
				else
					num[i][j] = num[i - 1][j] + num[i][j - 1];
			}
		}
		return num[m - 1][n - 1];
    }
}