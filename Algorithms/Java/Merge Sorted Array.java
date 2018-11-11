public class Solution {
    public void merge(int A[], int m, int B[], int n) {
		int i = 0, j = 0;
		while (i < m && j < n) {
			if (A[i] > B[j]) {
				for (int k = A.length - 1; k > i; k--) {
					A[k] = A[k - 1];
				}
				A[i] = B[j];
				i++;
				j++;
				m++;
			} else {
				i++;
			}
		}
		while (j < n) {
			A[i] = B[j];
			i++;
			j++;
		}
	}
}