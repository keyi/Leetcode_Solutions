public class Solution {
    public void sortColors(int[] A) {
		int left = 0;
		int right = A.length - 1;
		int index = 0;
		while (index <= right) {
			if (A[index] == 2)
				swap(A, index, right--);
			else if (A[index] == 0)
				swap(A, index++, left++);
			else
				index++;
		}
		return;
	}

	public void swap(int[] A, int a, int b) {
		int temp = A[b];
		A[b] = A[a];
		A[a] = temp;
		return;
	}
}