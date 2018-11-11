public class Solution {
    public int maxSubArray(int[] A) {
        int Max = A[0];
		for (int i = 0; i < A.length; i++) {
			if (Max < A[i])
				Max = A[i];
		}
		int sum = 0;
		for (int i : A) {
			if (sum > 0) {
				sum += i;
				if (sum > Max)
					Max = sum;
				continue;
			}
			if (i >= 0) {
				sum = 0;
				sum += i;
			}
		}
		return Max;
    }
}