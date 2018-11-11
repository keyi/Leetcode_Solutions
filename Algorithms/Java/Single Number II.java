public class Solution {
    public int singleNumber(int[] A) {
        int ans = 0;
		for (int i = 0; i < 32; i++) {
			int count = 0;
			for (int j = 0; j < A.length; j++) {
				count += (A[j] >> i) & 1;
			}
			count %= 3;
			ans |= (count << i);
		}
		return ans;
    }
}