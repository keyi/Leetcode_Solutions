public class Solution {
    public int climbStairs(int n) {
    	if (n < 2)
			return 1;
		int[] s = new int[n];
		s[0] = 1;
		s[1] = 2;
		for (int i = 2; i < n; i++)
			s[i] = s[i - 1] + s[i - 2];
		return s[n - 1]; 
    }
}